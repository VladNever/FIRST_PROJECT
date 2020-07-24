from django.urls import path
from books.views import CreateBooks, UpdateBooks, ListBooks, DeleteBooks
from books.views import DetailBooks, ListBooksManager, ListBooksSearch

app_name = "books"


urlpatterns = [
    path('create-books/', CreateBooks.as_view(), name="create"),
    path('update-books/<int:pk>', UpdateBooks.as_view(), name="update"),
    path('list-books/', ListBooks.as_view(), name="list"),
    path('delete-books/<int:pk>', DeleteBooks.as_view(), name="delete"),
    path('detail-books/<int:pk>', DetailBooks.as_view(), name="detail"),
    path('list-books-manager/', ListBooksManager.as_view(), name="list_manager"),
    path('list-books-search/', ListBooksSearch.as_view(), name="list_search"),
]