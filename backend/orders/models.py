from django.db import models
from users.models import User
from product.models import Product

# Create your models here.
choices = (
    ('Pending', 'Pending'),
    ('Packed', 'Packed'),
    ('Shipped', 'Shipped'),
    ('Delivered', 'Delivered')
)

class Order(models.Model):
    user = models.ForeignKey(User,
        related_name='orders', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        choices=choices, max_length=10, default='Pending')
    total_price = models.FloatField(null=False, blank=False)

    class Meta:
        ordering = ('-created',)

class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name='ordered', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total = models.FloatField(null=False, blank=False)

