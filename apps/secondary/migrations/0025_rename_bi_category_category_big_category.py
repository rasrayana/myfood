# Generated by Django 5.0.1 on 2024-01-07 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0024_news_remove_lastpost_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='bi_category',
            new_name='big_category',
        ),
    ]
