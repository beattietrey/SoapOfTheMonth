from django.shortcuts import render, redirect
from .models import *
from login.models import *
from application.models import *
from django.contrib import messages
import bcrypt

# display
def admin_dashboard(request):
    user = User.objects.get(id=request.session['id'])
    if 'id' not in request.session:
        return redirect('/')
    elif user.user_level != 5:
        return redirect('/dashboard')
    else:
        context={
            'admin':user
        }
        return render(request, 'admin_dashboard.html', context)

def inventory(request):
    context={
        'inventory': Product.objects.all()
    }
    return render(request, 'inventory_list.html', context)

def new_items(request):
    context={
        'user': User.objects.get(id=request.session['id'])
    }
    return render(request, 'add_item.html', context)

def user_profiles(request):
    context={
        'users': User.objects.all()
    }
    return render(request, 'user_profiles.html', context)

def orders(request):
    context={
        'orders': Order.objects.all()
    }

def edit_product(request, id):
    context={
        'user': User.objects.get(id= request.session['id']),
        'product': Product.objects.get(id=id)
    }
    return render(request, 'edit_item.html', context)

def add_ingredient_page(request):
    pass

# actions

def add_item_form(request):
    errors = Product.objects.product_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/admin/add_items')
    user = User.objects.get(id=request.session['id'])
    if 'id' not in request.session:
        return redirect('/')
    elif user.user_level != 5:
        return redirect('/dashboard')
    else:    
        if len(request.POST['cost_to_make'])> 0:
            cost=request.POST['cost_to_make']
        else:
            cost=0
        if len(request.POST['amount'])> 0:
            amount=request.POST['amount']
        else:
            amount=0
        if len(request.POST['description'])> 0:
            description=request.POST['description']
        else:
            description=""

        Product.objects.create(
        name=request.POST['product_name'],
        amount=amount,
        cost_to_make=cost,
        price=request.POST['price'],
        description=description,
    )
    return redirect('/admin/add_ingredients')

def edit_item_form(request):
    errors = Product.objects.product_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect(f"/admin/inventory/edit/{request.POST['product_id']}")
    user = User.objects.get(id=request.session['id'])
    if 'id' not in request.session:
        return redirect('/')
    elif user.user_level != 5:
        return redirect('/dashboard')
    else:
        product=Product.objects.get(id=request.POST['product_id'])
        product.name=request.POST['product_name']
        product.price=request.POST['price']
        if len(request.POST['cost_to_make'])> 0:
            product.cost_to_make=request.POST['cost_to_make']
        else:
            product.cost_to_make=0
        if len(request.POST['amount'])> 0:
            product.amount=request.POST['amount']
        else:
            product.amount=0
        if len(request.POST['description'])> 0:
            product.description=request.POST['description']
        else:
            product.description=""
        product.save()
        return redirect('/admin/inventory')

def delete_item(request, id):
    Product.objects.get(id=id).delete()
    return redirect('/admin/inventory')