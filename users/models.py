from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    image = models.ImageField(upload_to='user_images', blank=True, null=True)
    birth = models.DateField(blank=True, null=True)

    def safe_delete(self):
        self.is_active = False
        self.save()