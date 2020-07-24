from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView, DetailView, TemplateView, FormView
from .models import Order
from basket.models import Basket
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import Group

class CreateOrder(UpdateView):
    model = Order
    template_name = 'order/create_order.html'
    fields = ('delivery_address', 'contact_phone')

    def dispatch(self, request, *args, **kwargs):
        session_key = self.request.session.session_key
        basket = Basket.objects.filter(session_key=session_key)
        if basket:
            basket=basket.get()
            obj = basket.books.all()
            if obj:
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect('basket:list') 
        else:
            return redirect('basket:list')

    def get_object(self):
        session_key = self.request.session.session_key
        basket = Basket.objects.filter(session_key=session_key)
        basket=basket.get()
        if self.request.user.is_authenticated:
            order, created = Order.objects.get_or_create(
                basket = basket,
                defaults = {},
            )
            obj = order
        else:
            order, created = Order.objects.get_or_create(
                basket = basket,
                defaults = {},
            )
            obj = order

        return obj

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        self.request.session.delete()
        self.request.session.create()
        return super().form_valid(form)


    def get_success_url(self):
        return reverse_lazy('books:list')


class CanceledStatusOrder(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Order
    template_name = 'order/canceled_status.html'
    fields = ('cancel_order',)

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        
        "changing status"
        if self.object.cancel_order:
            self.object.status = Order.CANCELED
        else:
            self.object.status = Order.IN_PROCESSING

        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        if self.request.user.is_staff:
            return reverse_lazy('order:list_manager')
        else:
            return reverse_lazy('order:list')


class DeliveredStatusOrder(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    permission_required = 'order.view_all_orders'
    model = Order
    template_name = 'order/delivered_status.html'
    fields = ('deliver_order',)

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        
        "changing status"
        if self.object.deliver_order:
            self.object.status = Order.DELIVERED
        else:
            self.object.status = Order.IN_PROCESSING

        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        if self.request.user.is_staff:
            return reverse_lazy('order:list_manager')
        else:
            return reverse_lazy('order:list')


class ListOrders(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Order
    template_name = 'order/list_orders.html'
    
    def get_queryset(self):
        queryset = Order.objects.filter(basket__user=self.request.user).order_by('status', '-created')
        return queryset


class ListOrdersManager(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    permission_required = 'order.view_all_orders'
    model = Order
    template_name = 'order/list_orders_manager.html'
    ordering = ['status', '-created']


class DetailOrderManager(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    permission_required = 'order.view_all_orders'
    model = Order
    template_name = 'order/detail_order_manager.html'
    
    
    
    
    
    #def get_object(self):
    #    session_key = self.request.session.session_key
    #    obj = Basket.objects.filter(session_key=session_key)
    #    if obj:
    #        obj=obj.get()
    #        return obj
    #    else:
    #        return obj






#class ChangeStatusOrder(FormView):
#    model = Order
#    template_name = 'order/change_status.html'
#    form_class = ChangeStatusOrderForm
#    def get_object(self):
#
#        order_pk = self.request.GET.get('order_pk')
#        Order.objects.filter(id=order_pk).update(status=Order.CANCELED)
#        obj = super().get_object()
#        redirect('order:list')
#        return obj
#    def get_success_url(self):
#        return reverse_lazy('order:list')


#class ChangeStatusOrder(TemplateView):
#    template_name = 'order/list_orders.html'
#    extra_context = {
#        'Status': Books.objects.all(),
#        'Genre': Genre.objects.all(),
#        'last_added_books': Books.objects.all().order_by('-catalog_date')[:3],
#        'most_expensive': Books.objects.all().order_by('-price')[:3],
#    }
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        order_pk = self.request.GET.get('order_pk')
#        Order.objects.filter(id=order_pk).update(status=Order.CANCELED)
#        redirect('order:list')
#        return context
#


    #def get_object(self, queryset=None):
    #    obj = super().get_object()
    #    print(obj)
    #    print(type(obj))
    #    print('_____________________________________________________________________')
    #    Order.objects.filter(id=obj.pk).update(status=Order.CANCELED)
    #    redirect('order:list')
    #    #obj.objects.update(status=Order.CANCELED)
    #    return obj
    #
    #def get_success_url(self):
    #    return reverse_lazy('books:list')



#
#class DeleteBooksFromBasket(DeleteView):
#    login_url = reverse_lazy('login')
#    model = BookInBasket
#    template_name = 'basket/delete_books_from_basket.html'
#    def get_success_url(self):
#        return reverse_lazy('basket:list')

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


