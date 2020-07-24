from django.db import models

# Create your models here.

#Чтобы изменения попали в базу данных надо сделать:
#python manage.py makemigrations - создать миграции
#python manage.py migrate - отправить миграции в базу данных
class Genre(models.Model):
    name = models.CharField(
        verbose_name="Название Жанра",
        max_length=30
    )
    description = models.TextField(
        verbose_name="Описание Жанра",
        null=True,
        blank=True
    )
    class Meta:
        permissions = [
                    ("view_all_genres", "Can view all genres"),
                ]
    def __str__(self):
        return self.name

    
