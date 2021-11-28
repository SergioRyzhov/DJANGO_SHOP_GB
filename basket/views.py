from django.contrib import messages
from django.shortcuts import HttpResponseRedirect
from products.models import Product
from basket.models import Basket
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse

# Create your views here.

@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        basket = baskets.first()
        if basket.quantity <= product.quantity:
            basket.quantity += 1
            basket.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        else:
            messages.success(request, 'Количество заказанного товара превышает количество на складе')
            return HttpResponseRedirect(reverse('users:profile'))


@login_required
def basket_remove(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def basket_edit(request, id, quantity):
    if request.is_ajax():
        basket = Basket.objects.get(id=id)
        if quantity > 0:
            basket.quantity = quantity
            basket.save()
        else:
            basket.delete()
    # baskets = Basket.objects.filter(user=request.user)
    # context = {'baskets': baskets}
    result = render_to_string('basket/basket.html', context)
    return JsonResponse({'result': result})