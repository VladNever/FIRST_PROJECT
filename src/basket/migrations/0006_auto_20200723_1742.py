# Generated by Django 3.0.6 on 2020-07-23 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0005_auto_20200712_2052'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basket',
            options={'permissions': [('view_all_baskets', 'Can view all baskets')]},
        ),
    ]
