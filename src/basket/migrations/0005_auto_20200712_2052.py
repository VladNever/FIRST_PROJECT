# Generated by Django 3.0.6 on 2020-07-12 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0004_auto_20200712_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='session_key',
            field=models.CharField(max_length=40),
        ),
    ]
