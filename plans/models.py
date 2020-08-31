from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Plans(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(upload_to='images', default='image')

    def __str__(self):
        return self.title

