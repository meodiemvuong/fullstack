from django.urls import path
from product import views
urlpatterns = [
    path('products/', views.ProductGet.as_view() ),
    path('products/admin', views.ProductPost.as_view() ),
    path('products/<int:pk>', views.ProductDetail.as_view() ),
    path('products/admin/<int:pk>', views.ProductDetailAdmin.as_view() ),
]