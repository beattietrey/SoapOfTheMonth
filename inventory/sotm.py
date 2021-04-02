from .models import *
from login.models import *
from application.models import *
import random

def sotm(people,number_of_items,focused_items=[]):
    products = Product.objects.all()
    totalorder = []
    for customer in people:
        sotm_order = Order.objects.create(user=User.objects.get(id=customer.id))
        while len(sotm_order.products.all()) < number_of_items:
            new_product = products[random.randint(0,len(products)-1)]
            if new_product in customer.allergies.all():
                continue
            elif new_product in sotm_order.products.all():
                continue
            else:
                sotm_order.products.add(new_product)
        totalorder.append(sotm_order)
    return totalorder
