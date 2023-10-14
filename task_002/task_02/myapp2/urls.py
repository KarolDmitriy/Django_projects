from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('order_list/', views.order_list, name='order_list'),
    path('admin/', admin.site.urls),
    path('myapp2/', include('myapp2.urls')),
    path('customers/', views.create_customer, name='create_customer'),
    path('customers/<int:customer_id>/', views.read_customer, name='read_customer'),
    path('customers/<int:customer_id>/update/', views.update_customer, name='update_customer'),
    path('customers/<int:customer_id>/delete/', views.delete_customer, name='delete_customer'),
]
