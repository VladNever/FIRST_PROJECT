from django.db import models
from books.models import Books
from profiles.models import Profile


class Basket(models.Model):
    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        #primary_key = True
    )
    basket_date = models.DateTimeField(
        verbose_name="Дата создания корзины",
        auto_now=False,
        auto_now_add=True
    )
    basket_change_date = models.DateTimeField(
        verbose_name="Дата последнего изменения корзины",
        auto_now=True,
        auto_now_add=False
    )
    def __str__(self):
        return f'Basket #{self.pk}'


class BookInBasket(models.Model):
    basket = models.ForeignKey(
        Basket,
        on_delete=models.CASCADE,
        related_name='books'
    )
    book = models.ForeignKey(
        Books,
        on_delete=models.CASCADE,
        related_name='books_in_basket'
    )
    quantity = models.IntegerField(
        verbose_name="Quantity",
        default=1
    )
    book_in_basket_date = models.DateTimeField(
        verbose_name="Дата добавления книги в корзину",
        auto_now=False,
        auto_now_add=True
    )
    book_in_basket_change_date = models.DateTimeField(
        verbose_name="Дата последнего изменения добавленной книги",
        auto_now=True,
        auto_now_add=False
    )
    
    class Meta:
        unique_together = (('basket', 'book'),)

    def __str__(self):
        return f"Book #{self.book.pk} in basket #{self.basket.pk}"

