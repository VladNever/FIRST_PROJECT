from django.urls import path
from basket.views import AddBookToBasket, ListBooksInBasket, DeleteBooksFromBasket

app_name = "basket"


urlpatterns = [
    path('add/', AddBookToBasket.as_view(), name="add"),
    path('list/', ListBooksInBasket.as_view(), name="list"),
    path('delete/<int:pk>', DeleteBooksFromBasket.as_view(), name="delete"),

]