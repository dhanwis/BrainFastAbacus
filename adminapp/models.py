from django.db import models

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery')


class Event(models.Model):
    image = models.ImageField(upload_to='event')
    head = models.CharField(max_length=500, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)