# Generated by Django 3.0.6 on 2020-07-18 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0005_auto_20200712_2052'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='basket',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='order', to='basket.Basket'),
        ),
    ]
