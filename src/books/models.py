from django.db import models
from ref_books.models import Genre
# Create your models here.

#Чтобы изменения попали в базу данных надо сделать:
#python manage.py makemigrations - создать миграции
#python manage.py migrate - отправить миграции в базу данных
class Books(models.Model):
    name = models.CharField(
        verbose_name="Название книги",
        max_length=30
    )
    cover_photo = models.ImageField(
        verbose_name="Фото на обложке",
        upload_to="books-photo",
        null=True,
        blank=True
    )
    price = models.IntegerField(
        verbose_name="Цена (BYN)",
    )
    author = models.CharField(
        verbose_name="Автор",
        max_length=30
    )
    series = models.CharField(
        verbose_name="Серия",
        max_length=30
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        verbose_name="Жанр",
        null=True,
        blank=True
    )
    publishing_year = models.DateField(
        verbose_name="Год издания",
    )
    pages = models.IntegerField(
        verbose_name="Количество страниц",
    )
    binding = models.CharField(
        verbose_name="Переплёт",
        max_length=30
    )
    book_format = models.CharField(
        verbose_name="Формат книги",
        max_length=30
    )
    isbn = models.CharField(
        verbose_name="ISBN",
        max_length=30
    ) 
    weight = models.IntegerField(
        verbose_name="Вес книги (в граммах)",
    )
    age = models.IntegerField(
        verbose_name="Возрастные ограничения",
    )
    publishing = models.CharField(
        verbose_name="Издательство",
        max_length=30
    ) 
    in_stock = models.IntegerField(
        verbose_name="Количество книг в наличии",
    )
    active = models.BooleanField(
        verbose_name="Доступен для заказа"
    )
    rating = models.IntegerField(
        verbose_name="Рейтинг",
    )
    catalog_date = models.DateTimeField(
        verbose_name="Дата внесения в каталог",
        auto_now=False,
        auto_now_add=True
    )
    card_change_date = models.DateTimeField(
        verbose_name="Дата последнего изменения карточки",
        auto_now=True,
        auto_now_add=False
    )

    def __str__(self):
        return self.name
