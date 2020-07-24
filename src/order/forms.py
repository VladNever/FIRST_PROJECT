from django import forms
from .models import Order
from basket.models import Basket

class OrderForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = ['delivery_address', 'contact_phone']

#class ChangeStatusOrderForm(forms.ModelForm):
#    
#    class Meta:
#        model = Order
#        #fields = ['status',]