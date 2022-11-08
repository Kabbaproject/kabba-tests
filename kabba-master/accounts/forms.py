from dataclasses import field
from django.forms import ModelForm

from .models import Customer, Product,Service

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields ='__all__'
class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields ='__all__'
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields ='__all__'
