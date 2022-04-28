
from dataclasses import fields
from rest_framework import serializers
from orders.models import Order, OrderItem
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id','user', 'status', 'total_price')
        extra_kwargs = {
            'user': {'required': False},
            'total_price': {'required': False},
        }
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('id' ,'order', 'product', 'quantity', 'total')