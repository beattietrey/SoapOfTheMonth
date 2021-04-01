from django.urls import path,include     
from . import views

urlpatterns = [
    # display
    path('', views.success),
    path('user_info/<int:id>', views.edit_info),
    path('favorites/<int:id>', views.favorites),


    # action
    path('edit_user_info', views.edit_submit),
    
]