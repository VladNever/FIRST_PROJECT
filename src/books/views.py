from django.urls import reverse_lazy
from .models import Books
from .forms import BooksForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import ListView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.db.models import Q

# Для CREATE
# 1 Определить метод (GET или POST)
# 2 GET - создать форму, подкинуть её в контекст, показать страницу
# 3 POST - получить данные из POST-запроса, создать объкт, сохранить его в БД
# 4 Показать "другую" страницу (сообщение об успехе)

class CreateBooks(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    permission_required = 'books.add_books'
    model = Books
    form_class = BooksForm
    template_name = 'books/create_books.html'
    def get_success_url(self):
        return reverse_lazy('books:list_manager')


class UpdateBooks(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    permission_required = 'books.add_books'
    model = Books
    form_class = BooksForm
    template_name = 'books/update_books.html'
    def get_success_url(self):
        return reverse_lazy('books:list_manager')

class ListBooks(ListView):
    model = Books
    template_name = 'books/list_books.html'

class DeleteBooks(PermissionRequiredMixin, DeleteView):
    permission_required = 'books.add_books'
    model = Books
    template_name = 'books/delete_books.html'
    def get_success_url(self):
        return reverse_lazy('books:list_manager')

class DetailBooks(DetailView):
    model = Books
    template_name = 'books/detail_books.html'

class ListBooksManager(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    permission_required = 'books.view_all_books'
    model = Books
    template_name = 'books/list_books_manager.html'
    ordering = ['-catalog_date',]

class ListBooksSearch(ListView):
    model = Books
    template_name = 'books/list_books.html'

    def get_queryset(self):
        books = self.request.GET.get('q')
        object_list = Books.objects.filter(
            #Поиск без учёта верхнего регистра не работает для русских букв
            Q(name__icontains=books) | Q(author__icontains=books)
        )
        return object_list

     