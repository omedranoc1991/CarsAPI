from django.db import models

# Create your models here.

class Cars(models.Model):
    name = models.CharField(max_length=30)
    marca = models.CharField(max_length=20)
    precio = models.IntegerField()
