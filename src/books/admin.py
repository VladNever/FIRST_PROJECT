from django.contrib import admin
from .models import Books

# Register your models here.

#Создать суперпользователя - python manage.py createsuperuser

admin.site.register(Books)