from rest_framework import serializers
from product.models import Product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'image', 'description', 'category', 'price', 'amount')
    # def create(self, validated_data):
    #     instance = self.Meta.model(**validated_data)
    #     instance.save()
    #     return instance