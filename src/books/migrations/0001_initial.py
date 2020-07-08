# Generated by Django 3.0.6 on 2020-07-07 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ref_books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название книги')),
                ('cover_photo', models.ImageField(blank=True, null=True, upload_to='books-photo', verbose_name='Фото на обложке')),
                ('price', models.IntegerField(verbose_name='Цена (BYN)')),
                ('author', models.CharField(max_length=30, verbose_name='Автор')),
                ('series', models.CharField(max_length=30, verbose_name='Серия')),
                ('publishing_year', models.DateField(verbose_name='Год издания')),
                ('pages', models.IntegerField(verbose_name='Количество страниц')),
                ('binding', models.CharField(max_length=30, verbose_name='Переплёт')),
                ('book_format', models.CharField(max_length=30, verbose_name='Формат книги')),
                ('isbn', models.CharField(max_length=30, verbose_name='ISBN')),
                ('weight', models.IntegerField(verbose_name='Вес книги (в граммах)')),
                ('age', models.IntegerField(verbose_name='Возрастные ограничения')),
                ('publishing', models.CharField(max_length=30, verbose_name='Издательство')),
                ('in_stock', models.IntegerField(verbose_name='Количество книг в наличии')),
                ('active', models.BooleanField(verbose_name='Доступен для заказа')),
                ('rating', models.IntegerField(verbose_name='Рейтинг')),
                ('catalog_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата внесения в каталог')),
                ('card_change_date', models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения карточки')),
                ('genre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ref_books.Genre', verbose_name='Жанр')),
            ],
        ),
    ]
