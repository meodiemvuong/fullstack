from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)
    image = models.ImageField(upload_to='product/')
    description = models.TextField(max_length=2000)
    category = models.CharField(max_length=100)
    price = models.FloatField()
    amount = models.FloatField()
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)
    REQUIRED_FIELDS = []
