from django.db import models

class Gallery(models.Model):
    image = models.ImageField(upload_to='admin_app/door')
 