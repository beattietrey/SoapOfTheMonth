from django.db import models
from login.models import *
from application.models import *

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    products= models.ManyToManyField(Product, related_name='products')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)