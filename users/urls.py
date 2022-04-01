from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token 
from users import views
urlpatterns = [
    path('users/', views.UserList.as_view() ),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('login/', views.UserLogin.as_view()),
    path('logout/', views.UserLogout.as_view()),
    path('is_admin/',views.IsAdmin.as_view())

]