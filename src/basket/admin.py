from django.contrib import admin
from .models import Basket, BookInBasket

admin.site.register(Basket)
admin.site.register(BookInBasket)