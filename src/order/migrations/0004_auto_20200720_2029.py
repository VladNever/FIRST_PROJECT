# Generated by Django 3.0.6 on 2020-07-20 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20200719_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Отменён', 'Отменён'), ('В обработке', 'В обработке'), ('Завершено', 'Завершено')], default='В обработке', max_length=20, verbose_name='Статус'),
        ),
    ]
