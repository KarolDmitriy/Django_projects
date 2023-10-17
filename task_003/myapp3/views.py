from django.shortcuts import get_object_or_404, render
from .models import Customer, Product
from django.http import JsonResponse
from datetime import timedelta
from django.utils import timezone
from .forms import ProductEditForm

# Create a new customer
def create_customer(request):
    if request.method == 'POST':
        data = request.POST
        customer = Customer.objects.create(
            name=data['name'],
            email=data['email'],
            phone_number=data['phone_number'],
            address=data['address']
        )
        return JsonResponse({'message': 'Customer created successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'})

# Read a customer by ID
def read_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    data = {
        'id': customer.id,
        'name': customer.name,
        'email': customer.email,
        'phone_number': customer.phone_number,
        'address': customer.address,
        'registration_date': customer.registration_date
    }
    return JsonResponse(data)

# Update a customer by ID
def update_customer(request, customer_id):
    if request.method == 'POST':
        customer = get_object_or_404(Customer, pk=customer_id)
        data = request.POST
        customer.name = data['name']
        customer.email = data['email']
        customer.phone_number = data['phone_number']
        customer.address = data['address']
        customer.save()
        return JsonResponse({'message': 'Customer updated successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'})

# Delete a customer by ID
def delete_customer(request, customer_id):
    if request.method == 'POST':
        customer = get_object_or_404(Customer, pk=customer_id)
        customer.delete()
        return JsonResponse({'message': 'Customer deleted successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'})

def order_list(request):
    today = timezone.now()
    last_7_days = today - timedelta(days=7)
    last_30_days = today - timedelta(days=30)
    last_365_days = today - timedelta(days=365)

    last_7_days_products = Product.objects.filter(order__order_date__gte=last_7_days).distinct()
    last_30_days_products = Product.objects.filter(order__order_date__gte=last_30_days).distinct()
    last_365_days_products = Product.objects.filter(order__order_date__gte=last_365_days).distinct()

    return render(request, 'myapp3/order_list.html', {
        'last_7_days_products': last_7_days_products,
        'last_30_days_products': last_30_days_products,
        'last_365_days_products': last_365_days_products,
    })


def edit_product(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.method == 'POST':
        form = ProductEditForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            # Добавьте перенаправление или другие действия после успешного редактирования
    else:
        form = ProductEditForm(instance=product)

    return render(request, 'app_name/edit_product.html', {'form': form, 'product': product})