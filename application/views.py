from django.shortcuts import render, redirect
from .models import *
from login.models import *
from django.contrib import messages
import bcrypt

# display
def success(request):
    if 'id' not in request.session:
        return redirect('/')
    else:
        context={
            'user': User.objects.get(id=request.session['id'])
        }
        return render(request, 'home_page.html', context)

def edit_info(request, id):
    if 'id' not in request.session:
        return redirect('/')
    else:
        context={
            'user': User.objects.get(id=request.session['id']),
            'birth_date':datetime.strftime(User.objects.get(id=id).birth_date, "%Y-%m-%d"),
        }
        return render(request, 'edit_info.html', context)

def favorites(request, id):
    if 'id' not in request.session:
        return redirect('/')
    else:
        user=User.objects.get(id=request.session['id'])
        context={
            'user': user,
            'products': user.favorites.all(),
            'inventory': Product.objects.all(),
        }
    return render(request, 'favorites.html', context)







# action
def edit_submit(request):
    if 'id' not in request.session:
        return redirect('/')
    else:
        user=User.objects.get(id=request.session['id'])
        user.first_name=request.POST['first_name']
        user.last_name=request.POST['last_name']
        user.birth_date=request.POST['birth_date']
        user.email=request.POST['email']
        user.save()
        return redirect("/")