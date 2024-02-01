# Generated by Django 5.0.1 on 2024-01-06 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bron',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255, verbose_name='Полное имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('people', models.CharField(max_length=255, verbose_name='Человек')),
                ('phone', models.CharField(max_length=255, verbose_name='Номер телефона')),
                ('data', models.CharField(max_length=255, verbose_name='Дата')),
                ('time', models.CharField(max_length=255, verbose_name='Время')),
                ('message', models.TextField(verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Брон',
                'verbose_name_plural': 'Брон',
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('subject', models.CharField(max_length=255, verbose_name='Тема')),
                ('message', models.TextField(verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Обратная связь',
                'verbose_name_plural': 'Обратная связь',
            },
        ),
    ]
