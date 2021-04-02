from django.urls import path,include     
from . import views

urlpatterns = [
    # display
    path('', views.success),
    path('user_info/<int:id>', views.edit_info),
    path('favorites/<int:id>', views.favorites),
    path('allergies', views.allergies),
    path('new_order', views.new_order),
    



    # action
    path('edit_user_info', views.edit_submit),
    path('add_favorites', views.add_favorite),
    path('remove/<int:id>', views.remove_favorite),
    path('update_allergies', views.update_allergy),
    path('remove_allergies/<int:id>', views.remove_allergy),

    
] 