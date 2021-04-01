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

    # action
    path('add_inventory', views.add_item_form),
    path('edit_inventory', views.edit_item_form),
    path('item/<int:id>/delete', views.delete_item),

    
]