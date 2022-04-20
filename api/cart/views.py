from django.shortcuts import render
from rest_framework.views import Response, APIView
from rest_framework import permissions
from cart.cart import Cart
from product.models import Product
from product.serializers import ProductSerializer 
# Create your views here.
class CartAdd(APIView):
    permission_classes = [(permissions.IsAuthenticated)]
    def get(self, request):
        cart = Cart(request)
        
        return Response({'data': cart.session['cart']})
    def post(self, request):
        cart = Cart(request)
        id = request.data['id']
        product = Product.objects.get(pk=id)
        serializer = ProductSerializer(product)
        if(cart.cart.get(str(id))):
            quantity = cart.cart[str(id)].get('quantity') + 1 
            price = cart.cart[str(id)].get('price') + serializer.data['price']
            cart.session['cart'][str(id)] = {
                'quantity': quantity,
                'price': price
            }
            cart.save()
            return Response(cart.cart)
        else: 
            cart.add(id, serializer.data['price'])
            return Response(cart.cart)
        