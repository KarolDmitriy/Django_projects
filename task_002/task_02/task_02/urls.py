from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/', views.create_customer, name='create_customer'),
    path('customers/<int:customer_id>/', views.read_customer, name='read_customer'),
    path('customers/<int:customer_id>/update/', views.update_customer, name='update_customer'),
    path('customers/<int:customer_id>/delete/', views.delete_customer, name='delete_customer'),
    path('order_list/', include(myapp3.urls)),
]
