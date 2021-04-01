from django.urls import path     
from . import views

urlpatterns = [
    # display
    path('', views.registration_page),	   
    # path('success', views.success),


    # action
    path('register', views.registration),
    path('login', views.login),
    path('logout', views.logout),
    path('delete', views.deletedb),
]