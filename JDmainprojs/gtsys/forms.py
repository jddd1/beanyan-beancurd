from django.forms import ModelForm
from .models import *


class ProductForm(ModelForm):
	class Meta:
		model = Product
		fields = '__all__'


class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'


class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = ['status']