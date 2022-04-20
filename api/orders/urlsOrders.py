from django.urls import path
from orders import views
urlpatterns = [
    path('orders/', views.CreateOrder.as_view() ),
    path('orders/<int:pk>', views.OrderDetail.as_view())
]