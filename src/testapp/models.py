from django.db import models

# Create your models here.

#Чтобы изменения попали в базу данных надо сделать:
#python manage.py makemigrations - создать миграции
#python manage.py migrate - отправить миграции в базу данных
class Userrequests(models.Model):
    id_pr = models.AutoField(
        auto_created=True, 
        primary_key=True,
        serialize=False,
        verbose_name='ID'
    )
    ip_adr = models.CharField(
        verbose_name="IP адрес",
        max_length=20
    )
    date_request = models.DateField(
        verbose_name="Дата",
        default="0000-00-00"
    )
    safari = models.CharField(
        verbose_name="Safari",
        max_length=10,
        null=True,
        blank=True
    )
    firefox = models.CharField(
        verbose_name="Firefox",
        max_length=10,
        null=True,
        blank=True
    )
    unrefined_string = models.TextField(
        verbose_name="Запрос",
        null=True,
        blank=True
    )
    def __str__(self):
        return self.ip_adr

    