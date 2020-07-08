from django import forms
from .models import BookInBasket

class BooksForm(forms.ModelForm):
    
    class Meta:
        model = BookInBasket
        fields = ['quantity',]