# Generated by Django 5.0.1 on 2024-01-09 18:05

import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0040_rename_shopfood_food_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='image/', verbose_name='Фото изделий')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('price', models.CharField(max_length=255, verbose_name='Цена сейчас')),
            ],
            options={
                'verbose_name': 'Избранные',
                'verbose_name_plural': 'Избранные',
            },
        ),
    ]
