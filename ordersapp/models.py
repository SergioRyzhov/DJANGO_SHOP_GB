from django.conf import settings
from django.db import models
from django.db.models.fields import related
from products.models import Product

# Create your models here.

class Order(models.Model):
    FORMING = 'FM'
    SENT_TO_PROCEED = 'STP'
    PROCEEDED = 'PRD'
    PAID = 'PD'
    READY = 'RDY'
    CANCEL = 'CNC'
    FINISHED = 'FSD'
    
    ORDER_STATUS = (
        (FORMING, 'формируется'),
        (SENT_TO_PROCEED, 'отправлен в обработку'),
        (PAID, 'оплачен'),
        (PROCEEDED, 'обрабатывается'),
        (READY, 'готов к выдаче'),
        (FINISHED, 'завершен'),
        (CANCEL, 'отменен'),
    )    
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    
    created = models.DateTimeField(
        verbose_name='создан',
        auto_now_add=True,
    )
    
    updated = models.DateTimeField(
        verbose_name='изменен',
        auto_now=True,
    )
    
    status = models.CharField(
        verbose_name='статус',
        max_length=3,
        choices=ORDER_STATUS,
        default=FORMING,
    )
    
    is_active = models.BooleanField(
        verbose_name='активен',
        default=True
    )
    
    class Meta:
        ordering = ('-created',)
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
    
    def __str__(self):
        """returns order string
        """
        return f'заказ {self.user.name} №{self.id} от {self.created}'
    
    def get_total_quantity(self):
        """returns total quantity
        """
        items = self.orderitems.select_related()
        return sum(list(map(lambda x: x.quantity, items)))
    
    def get_product_type_quantity(self):
        """returns quantity of items
        """
        items = self.orderitems.select_related()
        return len(items)
    
    def get_total_cost(self):
        """returns summ of items
        """
        items = self.orderitems.select_related()
        return sum(list(map(lambda x: x.quantity * x.product.price, items)))
    
    def delete(self):
        """deletes item
        """
        for item in self.orderitems.select_related():
            item.product.quantity += item.quantity
            item.product.save()
            
        self.is_active = False
        self.save()
        
class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        related_name='orderitems',
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Product,
        verbose_name='продукт',
        on_delete=models.CASCADE,
    )
    quantity = models.PositiveIntegerField(
        verbose_name='количество',
        default=0,
    )
    
    def get_product_cost(self):
        """returns cost
        """
        return self.product.price * self.quantity
    