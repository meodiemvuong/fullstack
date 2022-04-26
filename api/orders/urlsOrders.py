from django.urls import path
from orders import views
from cart import views as viewsCart
urlpatterns = [
    path('orders/', views.CreateOrder.as_view() ),
    path('orders/<int:pk>', views.OrderDetail.as_view()),
    
]