from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView, DeleteView
from .models import Basket, BookInBasket
from books.models import Books
from django.contrib.auth.mixins import LoginRequiredMixin

class AddBookToBasket(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = BookInBasket
    template_name = 'basket/add_book.html'
    fields = ('quantity',)

    def get_object(self):
        #self.request.session.set_expiry(1)
        basket_pk = self.request.session.get('basket_pk')
        book_pk = self.request.GET.get('book_pk')
        book = Books.objects.get(pk=book_pk)
        user = self.request.user
        if bool(basket_pk) is True:
            basket = Basket.objects.get(
                pk=basket_pk,
                user = user,
            )
        else:
            basket = Basket.objects.create( 
                user = user,
            )
            self.request.session['basket_pk'] = basket.pk        
        obj, create = self.model.objects.get_or_create(
            basket = basket,
            book = book,
            defaults = {},
        )
        return obj 
    def get_success_url(self):
        return reverse_lazy('books:list')

class ListBooksInBasket(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = BookInBasket
    template_name = 'basket/list_books_in_basket.html'

class DeleteBooksFromBasket(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = BookInBasket
    template_name = 'basket/delete_books_from_basket.html'
    def get_success_url(self):
        return reverse_lazy('basket:list')