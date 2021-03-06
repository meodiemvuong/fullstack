from django.shortcuts import render
from rest_framework.views import APIView, Response
from orders.models import Order
from orders.serializers import OrderSerializer, OrderItemSerializer
from orders.models import OrderItem
from product.models import Product

from cart.cart import Cart
# Create your views here.

class CreateOrder(APIView):
    def get(self, request):
        order =Order.objects.filter(user=request.user)
        cart = Cart(request)
        serializer = OrderSerializer(order, many=True)
        return Response({'myorder': serializer.data, 'cart': cart.cart})
    def post(self, request):
        cart = Cart(request)
        if len(cart) == 0:
            return Response({'data': 'Gio hang trong'})
        total_price = cart.get_total_price()
        order = Order(user=self.request.user, total_price=total_price, status='Pending' )
        order.save()
        serializer = OrderSerializer(order)
        products = Product.objects.filter(id__in=cart.cart.keys())
        orderitems = []
        print(products)
        for i in products:
            print(i.id)
            q = cart.cart[str(i.id)]['quantity']
            orderitems.append(OrderItem(order=order,product = i, quantity = q, total = q*i.price ))
        OrderItem.objects.bulk_create(orderitems)
        cart.clear()
        return Response({'order': serializer.data})        

class OrderDetail(APIView):
    def get(self, request, pk):
        order = Order.objects.get(user=request.user, pk=pk)
        orderItem = OrderItem.objects.filter(order=order)
        serializer = OrderItemSerializer(orderItem, many=True)
        print(orderItem)
        return Response(serializer.data)