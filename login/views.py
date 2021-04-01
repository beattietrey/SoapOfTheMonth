from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

# display
def registration_page(request):
    if 'id' in request.session:
        return redirect('/dashboard')
    else:
        return render(request,'registration.html')

def success(request):
    if 'id' not in request.session:
        return redirect('/')
    else:
        context={
            'how': request.session['how'],
            'user': User.objects.get(id=request.session['id'])
        }
        return render(request, 'home_page.html', context)







# actions

def registration(request):
    errors = User.objects.reg_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/')
    else:
        password=request.POST['password']
        
        user = User.objects.create(
            first_name=request.POST['fName'],
            last_name=request.POST['lName'],
            birth_date=request.POST['birthday'],
            email=request.POST['email'],
            password=bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode(),
        )
        how = 'register'
        context={
            user,
            how
        }
        
        request.session['how']='reg'
        request.session['id']=user.id
        request.session['level']=user.user_level
        return redirect('/dashboard')
    

def login(request):
    user= User.objects.filter(email=request.POST['email'])
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/')
    if user:
        logged_user = user[0]
        request.session['id']= logged_user.id
        request.session['how']='login'
        request.session['level']=logged_user.user_level
        return redirect('/dashboard')
    else: 
        print("invalid login")
        return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def deletedb(request):
    User.objects.all().delete()
    print('Deleted all users')
    return redirect('/')