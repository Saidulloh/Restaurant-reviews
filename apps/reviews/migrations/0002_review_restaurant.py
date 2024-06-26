# Generated by Django 4.1.5 on 2024-04-04 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_restaurant_latitude_restaurant_longitude'),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='restaurant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='restaurant', to='restaurants.restaurant', verbose_name='restaurant'),
            preserve_default=False,
        ),
    ]
