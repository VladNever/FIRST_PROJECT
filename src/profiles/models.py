from django.db import models
from django.contrib.auth.models import AbstractUser

class Profile(AbstractUser):
    phone_number = models.CharField(
        verbose_name="Мобильный номер телефона",
        max_length=30,
        null=True,
        blank=True
    )
    country = models.CharField(
        verbose_name="Страна",
        max_length=30,
        null=True,
        blank=True
    )
    city = models.CharField(
        verbose_name="Город",
        max_length=30,
        null=True,
        blank=True
    )
    index = models.CharField(
        verbose_name="Индекс",
        max_length=30,
        null=True,
        blank=True
    )
    adress1 = models.CharField(
        verbose_name="Адрес прописки",
        max_length=40,
        null=True,
        blank=True
    ) 
    adress2 = models.CharField(
        verbose_name="Адрес проживания",
        max_length=40,
        null=True,
        blank=True
    )
    additionally = models.TextField(
        verbose_name="Дополнительная информация",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.first_name



