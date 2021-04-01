from django.db import models
import re
from datetime import datetime, date,timedelta
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def reg_validator(self,postData):
        today = datetime.today()
        t=timedelta(-4745)
        errors ={}

        if len(postData['fName']) < 2:
            errors['fName'] = 'First and Last name must be at least 2 characters'
        if len(postData['lName']) < 2:
            errors['lName'] = 'First and Last name must be at least 2 characters'
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):             
            errors['email'] = "Invalid email address!"
        if len(User.objects.filter(email=postData['email'])) >0:
            errors['email'] = 'Email must be original'
        if len(postData['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters'
        if postData['confirm_password'] != postData['password']:
            errors['password'] = 'Password must Match'
        if len(postData['birthday']) < 10:
            errors['birthday'] = 'Valid birth date is required'
        elif datetime.strptime(postData['birthday'], "%Y-%m-%d") > today+t:
            errors['birthday'] = "Must be at least 13 years old"
        return errors
    
    def login_validator(self,postData):
        errors={}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(User.objects.filter(email=postData['email'])) < 1:
            errors['login'] = 'Invalid login credentials'
        else:
            user= User.objects.filter(email=postData['email'])
            logged_user=user[0]
            if not EMAIL_REGEX.match(postData['email']):             
                errors['email'] = "Invalid email address!"
            if not postData['email'] not in User.objects.filter(email=postData['email']):
                errors['login'] = 'Invalid login credentials'
            if not bcrypt.checkpw(postData['password'].encode(), logged_user.password.encode()):
                errors['login']= 'Invalid login credentials'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    birth_date = models.DateField()
    email = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    password=models.CharField(max_length=100)
    updated_at=models.DateTimeField(auto_now=True)
    user_level=models.IntegerField(default=0)
    objects=UserManager()

