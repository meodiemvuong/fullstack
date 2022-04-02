from asyncio.windows_events import NULL
from enum import unique
from unicodedata import category
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(unique=True, max_length=100)
    image = models.ImageField(upload_to='product/')
    description = models.TextField(max_length=2000)
    category = models.CharField(max_length=100)
    price = models.FloatField()
    amount = models.FloatField()
def __str__(self):
    return self.title