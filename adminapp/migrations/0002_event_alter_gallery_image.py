# Generated by Django 5.1.3 on 2024-12-07 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='admin_app/event')),
                ('head', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(upload_to='admin_app/gallery'),
        ),
    ]