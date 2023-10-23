from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.create_customer, name='create_customer'),
    path('customers/<int:customer_id>/', views.read_customer, name='read_customer'),
    path('customers/<int:customer_id>/update/', views.update_customer, name='update_customer'),
    path('customers/<int:customer_id>/delete/', views.delete_customer, name='delete_customer'),
    path('order_list/', views.order_list, name='order_list'),
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
]
