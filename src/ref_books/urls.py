from django.urls import path
from ref_books.views import CreateGenre, UpdateGenre, ListGenre, DeleteGenre, DetailGenre

app_name = "ref_books"


urlpatterns = [
    path('create-genre/', CreateGenre.as_view(), name="create_genre"),
    path('update-genre/<int:pk>', UpdateGenre.as_view(), name="update_genre"),
    path('list-genre/', ListGenre.as_view(), name="list_genre"),
    path('delete-genre/<int:pk>', DeleteGenre.as_view(), name="delete_genre"),
    path('detail-genre/<int:pk>', DetailGenre.as_view(), name="detail_genre"),
]