# Generated by Django 5.2 on 2025-04-30 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurantinfo',
            name='restaurant',
        ),
        migrations.DeleteModel(
            name='GalleryImage',
        ),
        migrations.DeleteModel(
            name='RestaurantInfo',
        ),
    ]
