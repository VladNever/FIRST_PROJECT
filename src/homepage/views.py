from django.urls import reverse_lazy
from books.models import Books
from ref_books.models import Genre
from django.views.generic import TemplateView

# Create your views here.

# Для CREATE
# 1 Определить метод (GET или POST)
# 2 GET - создать форму, подкинуть её в контекст, показать страницу
# 3 POST - получить данные из POST-запроса, создать объкт, сохранить его в БД
# 4 Показать "другую" страницу (сообщение об успехе)

class HomePage(TemplateView):
    template_name = 'homepage/homepage.html'
    extra_context = {
        'Books': Books.objects.all(),
        'Genre': Genre.objects.all(),
        'last_added_books': Books.objects.all().order_by('-catalog_date')[:3],
        'most_expensive': Books.objects.all().order_by('-price')[:3],
    } 
   



    #def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    
    #    kwargs.setdefault('view', self)
    #    if self.extra_context is not None:
    #        kwargs.update(self.extra_context)
    #    return kwargs

