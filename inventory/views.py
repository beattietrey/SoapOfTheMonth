from django.shortcuts import render, redirect
from .models import *
from login.models import *
from application.models import *
from django.contrib import messages
import bcrypt
from inventory.sotm import *

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
    user = User.objects.get(id=request.session['id'])
    if 'id' not in request.session:
        return redirect('/')
    elif user.user_level != 5:
        return redirect('/dashboard')
    else:
        context={
            'user': user,
            'inventory': Product.objects.all()
        }
        return render(request, 'inventory_list.html', context)

def new_items(request):
    user = User.objects.get(id=request.session['id'])
    if 'id' not in request.session:
        return redirect('/')
    elif user.user_level != 5:
        return redirect('/dashboard')
    else:
        context={
            'user': User.objects.get(id=request.session['id'])
        }
        return render(request, 'add_item.html', context)

def user_profiles(request):
    user = User.objects.get(id=request.session['id'])
    if 'id' not in request.session:
        return redirect('/')
    elif user.user_level != 5:
        return redirect('/dashboard')
    else:
        context={
            'admin':User.objects.get(id=request.session['id']),
            'users': User.objects.all()
        }
        return render(request, 'users.html', context)

def user_profiles_edit(request, id):
    admin = User.objects.get(id=request.session['id'])
    if 'id' not in request.session:
        return redirect('/')
    elif admin.user_level != 5:
        return redirect('/dashboard')
    else:
        context={
            'admin':User.objects.get(id=request.session['id']),
            'user': User.objects.get(id=id),
            'birth_date':datetime.strftime(User.objects.get(id=id).birth_date, "%Y-%m-%d"),
        }
        return render(request, 'edit_users.html', context)

def orders(request):
    user = User.objects.get(id=request.session['id'])
    if 'id' not in request.session:
        return redirect('/')
    elif user.user_level != 5:
        return redirect('/dashboard')
    else:
        context={
            'admin' :User.objects.get(id=request.session['id']),
            'users': User.objects.all(),
            'orders': Order.objects.all()
        }
        return render(request,'orders.html', context)

def edit_product(request, id):
    user = User.objects.get(id=request.session['id'])
    if 'id' not in request.session:
        return redirect('/')
    elif user.user_level != 5:
        return redirect('/dashboard')
    else:
        context={
            'user': User.objects.get(id= request.session['id']),
            'product': Product.objects.get(id=id),
            'ingredients': Ingredient.objects.all()
        }
        return render(request, 'edit_item.html', context)

def add_ingredient_page(request, id):
    user = User.objects.get(id=request.session['id'])
    if 'id' not in request.session:
        return redirect('/')
    elif user.user_level != 5:
        return redirect('/dashboard')
    else:
        context={
            'product': Product.objects.get(id=id),
            'ingredients': Ingredient.objects.all(),
            'user': User.objects.get(id= request.session['id']),
        }
        return render(request, 'add_ingr_page.html', context)

def new_ingredient_page(request):
    user = User.objects.get(id=request.session['id'])
    if 'id' not in request.session:
        return redirect('/')
    elif user.user_level != 5:
        return redirect('/dashboard')
    else:
        context={
            'ingredients': Ingredient.objects.all()
        }
        return render(request, 'new_ingr_page.html', context)


def sotm_table(request):
    users = User.objects.all()
    products = Product.objects.all()
    order = sotm(users,3)
    context={
        'admin': User.objects.get(id=request.session['id']), 
        'order': order,
    }
    return render(request, 'sotm_table.html', context)

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

        product = Product.objects.create(
        name=request.POST['product_name'],
        amount=amount,
        cost_to_make=cost,
        price=request.POST['price'],
        description=description,
        )
    return redirect(f'/admin/add_ing_page/{product.id}')

def edit_item_form(request):
    # errors = Product.objects.product_validator(request.POST)
    # if len(errors) > 0:
    #     for key, value in errors.items():
    #         messages.error(request,value)
    #     return redirect(f"/admin/inventory/edit/{request.POST['product_id']}")
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
        for ingredient in request.POST['ingredients']:
            if True:
                if ingredient not in product.ingredients.all():
                    product.ingredients.add(ingredient)
            if False:
                if ingredient in product.ingredients.all():
                    product.ingredients.remove(ingredient)

        product.save()
        return redirect('/admin/inventory')

def delete_item(request, id):
    user = User.objects.get(id=request.session['id'])
    if 'id' not in request.session:
        return redirect('/')
    elif user.user_level != 5:
        return redirect('/dashboard')
    else:
        Product.objects.get(id=id).delete()
        return redirect('/admin/inventory')

def add_ing(request,id):
    user = User.objects.get(id=request.session['id'])
    if 'id' not in request.session:
        return redirect('/')
    elif user.user_level != 5:
        return redirect('/dashboard')
    else:
        product=Product.objects.get(id=id)
        product.ingredients.add(request.POST['ingredients'])
        product.save()
        return redirect("/admin/inventory")

def new_ing(request):
    user = User.objects.get(id=request.session['id'])
    if 'id' not in request.session:
        return redirect('/')
    elif user.user_level != 5:
        return redirect('/dashboard')
    else:
        Ingredient.objects.create(
            name=request.POST['new_ing']
        )
        Allergy.objects.create(
            name=request.POST['new_ing']
        )
        product=Product.objects.get(id=request.POST['product_id'])
        return redirect(f'/admin/add_ing_page/{product.id}')

def edit_user(request, id):
    admin = User.objects.get(id=request.session['id'])
    if 'id' not in request.session:
        return redirect('/')
    elif admin.user_level != 5:
        return redirect('/dashboard')
    else:
        user = User.objects.get(id=id)
        user.first_name= request.POST['first_name']
        user.last_name= request.POST['last_name']
        user.bith_date= request.POST['birth_date']
        user.email= request.POST['email']
        user.user_level= request.POST['level']
        user.save()
        return redirect('/admin/users')

