from django.urls import reverse_lazy
from .models import Genre
from .forms import GenreForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
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

class CreateGenre(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    permission_required = 'ref_books.add_genre'
    model = Genre
    form_class = GenreForm
    template_name = 'ref_books/create_genre.html'
    def get_success_url(self):
        return reverse_lazy('ref_books:ref_books_manager')

class UpdateGenre(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    permission_required = 'ref_books.change_genre'
    model = Genre
    form_class = GenreForm
    template_name = 'ref_books/update_genre.html'
    def get_success_url(self):
        return reverse_lazy('ref_books:ref_books_manager')
        #return reverse_lazy('genre:list', kwargs={'pk': self.object.pk})

class ListGenre(ListView):
    model = Genre
    template_name = 'ref_books/list_genre.html'

class DeleteGenre(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    permission_required = 'ref_books.delete_genre'
    model = Genre
    template_name = 'ref_books/delete_genre.html'
    def get_success_url(self):
        return reverse_lazy('ref_books:ref_books_manager')

class DetailGenre(DetailView):
    model = Genre
    template_name = 'ref_books/detail_genre.html'

class RefBooksManager(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    permission_required = 'ref_books.view_all_genres'
    model = Genre
    template_name = 'ref_books/ref_books_manager.html'

    def get_success_url(self):
        return reverse_lazy('ref_books:ref_books_manager')




#class Test(TemplateView):
#    template_name = 'genres/test.html'
#    
#    def get_context_data(self, **kwargs):
#        # 1. Берём родительский метод применя метода super() 
#        # 2. Добавляем своих параметров  
#        context = super().get_context_data(**kwargs)
#        context['rate'] = self.get_rate()
#        return context
#    def get_rate(self):
#        return 2.755
     
