from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView, DeleteView, DetailView
from .models import Basket, BookInBasket
from books.models import Books
from django.contrib.auth.mixins import LoginRequiredMixin

class AddBookToBasket(UpdateView):
    login_url = reverse_lazy('login')
    model = BookInBasket
    template_name = 'basket/add_book.html'
    fields = ('quantity',)

    def get_object(self):
        book_pk = self.request.GET.get('book_pk')
        book = Books.objects.get(pk=book_pk)
        user = self.request.user
        if self.request.user.is_authenticated:
            basket, created = Basket.objects.get_or_create(
                user = user,
                session_key = self.request.session.session_key,
            )
            obj, create = self.model.objects.get_or_create(
                basket = basket,
                book = book,
                defaults = {},
            )
            return obj
        else:
            if not self.request.session.session_key:
                self.request.session.save()
                session_key = self.request.session.session_key
            else:
                session_key = self.request.session.session_key
            basket, created = Basket.objects.get_or_create(
                session_key = session_key,
                defaults = {'user': None}
            )
            obj, create = self.model.objects.get_or_create(
                basket = basket,
                book = book,
                defaults = {},
            )
            return obj
    def get_success_url(self):
        return reverse_lazy('books:list')



class ListBooksInBasket(DetailView):
    login_url = reverse_lazy('login')
    model = Basket
    template_name = 'basket/list_books_in_basket.html'
    def get_object(self):
        session_key = self.request.session.session_key
        obj = Basket.objects.filter(session_key=session_key)
        if obj:
            obj=obj.get()
            return obj
        else:
            return obj


    #def get_queryset(self):
    #    queryset = BookInBasket.objects.filter(
    #        basket__session_key=self.request.session.session_key,
    #    )
    #    return queryset

class DeleteBooksFromBasket(DeleteView):
    login_url = reverse_lazy('login')
    model = BookInBasket
    template_name = 'basket/delete_books_from_basket.html'
    def get_success_url(self):
        return reverse_lazy('basket:list')

        #def get_object(self):
        ##self.request.session.set_expiry(1)
        #basket_pk = self.request.session.get('basket_pk')
        #book_pk = self.request.GET.get('book_pk')
        #book = Books.objects.get(pk=book_pk)
        #user = self.request.user
        #if self.request.user.is_authenticated:
        #    if bool(basket_pk) is True:
        #        basket = Basket.objects.get(
        #            pk=basket_pk,
        #            user = user,
        #        )
        #    else:
        #        basket = Basket.objects.create(
        #            user = user,
        #        )
        #        self.request.session['basket_pk'] = basket.pk
        #    obj, create = self.model.objects.get_or_create(
        #        basket = basket,
        #        book = book,
        #        defaults = {},
        #    )
        #    return obj
        #else:
        #    basket, created = Basket.objects.get_or_create(
        #        session_key = self.request.session.session_key,
        #        defaults = {'user': None}
        #    )
        #    obj, create = self.model.objects.get_or_create(
        #        basket = basket,
        #        book = book,
        #        defaults = {},
        #    )
        #    return obj