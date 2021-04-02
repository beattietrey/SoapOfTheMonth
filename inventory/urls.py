from django.urls import path,include     
from . import views

urlpatterns = [
    # display
    path('', views.admin_dashboard),
    path('inventory', views.inventory),
    path('add_items', views.new_items),
    path('users', views.user_profiles),
    path('orders', views.orders),
    path('inventory/edit/<int:id>', views.edit_product),
    path('add_ing_page/<int:id>', views.add_ingredient_page),
    path('users', views.user_profiles),
    path('users/search', views.user_profiles),
    path('users/edit/<int:id>', views.user_profiles_edit),
    path('soap_of_the_month', views.sotm_table),

    # action
    path('add_inventory', views.add_item_form),
    path('edit_inventory', views.edit_item_form),
    path('edit_user/<int:id>', views.edit_user),
    path('item/<int:id>/delete', views.delete_item),
    path('add_ing/<int:id>', views.add_ing),
    path('new_ing', views.new_ing),    
]