# Generated by Django 3.0.6 on 2020-06-07 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название Жанра')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание Жанра')),
            ],
        ),
    ]
