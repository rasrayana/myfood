# Generated by Django 5.0.1 on 2024-01-08 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0033_review_remove_news_comment_remove_news_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='comment',
            new_name='comments',
        ),
    ]