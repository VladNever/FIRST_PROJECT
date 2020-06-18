from django import forms
from .models import Books

class BooksForm(forms.ModelForm):
    
    class Meta:
        model = Books
        fields = ['name', 'cover_photo', 'price', 'author', 'series', 'genre', 'publishing_year',
                  'pages', 'binding', 'book_format', 'isbn', 'weight', 'age', 'publishing', 'in_stock', 'active',
                  'rating']