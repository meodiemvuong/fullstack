from multiprocessing import context
from urllib import request
from django.shortcuts import render
from rest_framework import permissions
# from rest_framework.decorators import permission_classes
from rest_framework import generics
from product.models import Product
from product.serializers import ProductSerializer
# Create your views here.

class ProductGet(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductPost(generics.ListCreateAPIView):
    permission_classes = [(permissions.IsAdminUser)]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailAdmin(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [(permissions.IsAdminUser)]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

