
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
        except KeyError:
            raise exceptions.APIException("Request dont have id")
        try:
            product = Product.objects.get(pk=id)
        except Product.DoesNotExist:
            raise exceptions.APIException("Dont find Product")
        serializer = ProductSerializer(product)
        product_patch = ProductSerializer(product, data={'amount': serializer.data['amount']-1}, partial=True)
        if product_patch.is_valid():
            product_patch.save()
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
