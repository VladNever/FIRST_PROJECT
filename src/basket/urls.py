from django.urls import path
from basket.views import AddBookToBasket, ListBooksInBasket, DeleteBooksFromBasket, ListBasketsManager, DeatailBasketsManager

app_name = "basket"


urlpatterns = [
    path('add/', AddBookToBasket.as_view(), name="add"),
    path('list/', ListBooksInBasket.as_view(), name="list"),
    path('delete/<int:pk>', DeleteBooksFromBasket.as_view(), name="delete"),
    path('list_manager/', ListBasketsManager.as_view(), name="list_manager"),
    path('detail_manager/<int:pk>', DeatailBasketsManager.as_view(), name="detail_manager"),
]