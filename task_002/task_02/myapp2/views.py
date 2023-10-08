from django.shortcuts import get_object_or_404
from .models import Customer
from django.http import JsonResponse

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
