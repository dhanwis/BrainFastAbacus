# Generated by Django 5.1.3 on 2024-12-30 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0007_news_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='image',
        ),
    ]