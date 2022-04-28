
from rest_framework.views import Response, APIView
from rest_framework import permissions, exceptions
from cart.cart import Cart
from product.models import Product
from product.serializers import ProductSerializer 
# Create your views here.
class CartAdd(APIView):
    permission_classes = [(permissions.IsAuthenticated)]
    def get(self, request):
        cart = Cart(request)
        return Response(cart.cart)
    def post(self, request):
        cart = Cart(request)
        try:
            id = request.data['id']
            amount = request.data['quantity']
        except KeyError:
            raise exceptions.APIException("Request dont have id or quantity")
        try:
            product = Product.objects.get(pk=id)
        except Product.DoesNotExist:
            raise exceptions.APIException("Dont find Product")
        serializer = ProductSerializer(product)
        if serializer.data['amount'] > amount:
            product_patch = ProductSerializer(product, data={'amount': serializer.data['amount']-amount}, partial=True)
        else:
            raise exceptions.APIException('Out of stock')
        if product_patch.is_valid():
            product_patch.save()
        if(cart.cart.get(str(id))):
            quantity = cart.cart[str(id)].get('quantity') + amount 
            price = cart.cart[str(id)].get('price') + serializer.data['price']*amount
            cart.session['cart'][str(id)] = {
                'quantity': quantity,
                'price': price
            }
            cart.save()
            
            return Response(cart.cart)
        else:
            cart.add(id, serializer.data['price']*amount,amount)
            return Response(cart.cart)
