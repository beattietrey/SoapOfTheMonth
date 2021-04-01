from django.db import models
from login.models import *

# Create your models here.

class ProductManager(models.Manager):
    def product_validator(self, postData):
        user = User.objects.get(id=postData['id'])
        errors={}
        
        if len(postData['product_name']) < 1:
            errors['product_name'] = 'Product must have a name'
        if len(postData['price'])  < 1:
            errors['price'] = 'Price must be set'
        if user.user_level != 5:
            errors['admin'] = 'Invalid Admin Access'
        return errors

class Allergy(models.Model):
    name=models.CharField(max_length=45)
    serverity= models.TextField()
    users = models.ManyToManyField(User, related_name='allergies')

class Product(models.Model):
    name=models.CharField(max_length=255)
    amount=models.TextField(default=0)
    cost_to_make=models.DecimalField(max_digits=6, decimal_places=2, default=0)
    price=models.CharField(max_length=10)
    description=models.TextField(default='')
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    users=models.ManyToManyField(User, related_name='favorites')
    objects=ProductManager()

class Ingredient(models.Model):
    name=models.CharField(max_length=45)
    products=models.ManyToManyField(Product, related_name='ingredients')