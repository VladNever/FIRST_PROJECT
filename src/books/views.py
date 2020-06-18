from django.urls import reverse_lazy
from .models import Books
from .forms import BooksForm
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import ListView
from django.views.generic import DeleteView
from django.views.generic import DetailView
# Create your views here.

# Для CREATE
# 1 Определить метод (GET или POST)
# 2 GET - создать форму, подкинуть её в контекст, показать страницу
# 3 POST - получить данные из POST-запроса, создать объкт, сохранить его в БД
# 4 Показать "другую" страницу (сообщение об успехе)

class CreateBooks(CreateView):
    model = Books
    form_class = BooksForm
    template_name = 'books/create_books.html'
    def get_success_url(self):
        return reverse_lazy('books:list')

class UpdateBooks(UpdateView):
    model = Books
    form_class = BooksForm
    template_name = 'books/update_books.html'
    def get_success_url(self):
        return reverse_lazy('books:list')

class ListBooks(ListView):
    model = Books
    template_name = 'books/list_books.html'

class DeleteBooks(DeleteView):
    model = Books
    template_name = 'books/delete_books.html'
    def get_success_url(self):
        return reverse_lazy('books:list')

class DetailBooks(DetailView):
    model = Books
    template_name = 'books/detail_books.html'



     