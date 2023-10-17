from django import forms
from .models import Product

class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'photo']
