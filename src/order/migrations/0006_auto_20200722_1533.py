# Generated by Django 3.0.6 on 2020-07-22 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20200721_1540'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'permissions': [('view_all_orders', 'Can view all orders')]},
        ),
    ]
