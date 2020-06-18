from django.urls import path
from genres.views import CreateGenre, UpdateGenre, ListGenre, DeleteGenre, DetailGenre

app_name = "genre"


urlpatterns = [
    path('create-genre/', CreateGenre.as_view(), name="create"),
    path('update-genre/<int:pk>', UpdateGenre.as_view(), name="update"),
    path('list-genre/', ListGenre.as_view(), name="list"),
    path('delete-genre/<int:pk>', DeleteGenre.as_view(), name="delete"),
    path('detail-genre/<int:pk>', DetailGenre.as_view(), name="detail"),
]