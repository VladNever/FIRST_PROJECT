from .models import Genre
from .forms import GenreForm
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import ListView
from django.views.generic import DeleteView
# Create your views here.

# Для CREATE
# 1 Определить метод (GET или POST)
# 2 GET - создать форму, подкинуть её в контекст, показать страницу
# 3 POST - получить данные из POST-запроса, создать объкт, сохранить его в БД
# 4 Показать "другую" страницу (сообщение об успехе)

class CreateGenre(CreateView):
    # id не нужен
    # куда сохранять?
    model = Genre
    # какую форму будем использовать
    form_class = GenreForm
    # в каком шаблоне всё это отрисовывать?
    template_name = 'testapp/create_genre.html'
    success_url = "/list-genre"

class UpdateGenre(UpdateView):
    model = Genre
    form_class = GenreForm
    template_name = 'testapp/update_genre.html'
    success_url = "/list-genre"

class ListGenre(ListView):
    model = Genre
    template_name = 'testapp/list_genre.html'

class DeleteGenre(DeleteView):
    model = Genre
    template_name = 'testapp/delete_genre.html'
    success_url = "/list-genre"





#class Test(TemplateView):
#    template_name = 'testapp/test.html'
#    
#    def get_context_data(self, **kwargs):
#        # 1. Берём родительский метод применя метода super() 
#        # 2. Добавляем своих параметров  
#        context = super().get_context_data(**kwargs)
#        context['rate'] = self.get_rate()
#        return context
#    def get_rate(self):
#        return 2.755
     