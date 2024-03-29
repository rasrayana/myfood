# Generated by Django 5.0.1 on 2024-01-05 13:42

import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0016_alter_lastpost_instagram'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlideAbout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='imagelast/', verbose_name='Задняя фотография')),
            ],
            options={
                'verbose_name': 'Главное фото О нас',
                'verbose_name_plural': 'Главное фото О нас',
            },
        ),
    ]
