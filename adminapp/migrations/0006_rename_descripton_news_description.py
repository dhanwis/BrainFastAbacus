# Generated by Django 5.1.3 on 2024-12-26 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0005_news'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='descripton',
            new_name='description',
        ),
    ]