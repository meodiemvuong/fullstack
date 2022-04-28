from django.contrib import auth
from rest_framework.views import APIView, Response
from rest_framework.authtoken.models import Token
from users.models import User
from users.serializers import UserSerializer
from rest_framework import exceptions
from rest_framework import permissions
from rest_framework import exceptions
from rest_framework.decorators import permission_classes
# Create your views here.
class UserList(APIView):
    permission_classes = [(permissions.IsAdminUser)]
    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        user = User.objects.get(id=serializer.data.get('id'))
        token, created = Token.objects.get_or_create(user = user)
        return Response({"data": serializer.data,"token": token.key })

class UserDetail(APIView):
    permission_classes = [(permissions.IsAdminUser)]
    def get(self,request,pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        token, created = Token.objects.get_or_create(user = user)
        return Response({"data": serializer.data,"token": token.key })

class UserLogin(APIView):

    def post(self, request):
        username = request.data['username']
        if not username:
            return None

        try:
            user = User.objects.get(username=username)
        
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        serializer = UserSerializer(user)
        if not (user.check_password(request.data['password'])):
            return Response({"message": "Sai mat khau"})
        is_admin = user.is_staff
        auth.login(request, user=user)
        print(user)
        token, created = Token.objects.get_or_create(user = user)
        response = Response()
        response.set_cookie('Token',token)
        response.data = {
            'Token': token.key,
            'data': serializer.data,
            'is_admin': is_admin,
        }
        return response
        
class UserLogout(APIView):
    def post(self, request):
        print("hello")
        auth.logout(request)
        response = Response()
        response.delete_cookie('Token')
        response.data = {
            'message': "Thanh cong"
        }
        return response

class IsAdmin(APIView):
    # permission_classes = [(permissions.IsAuthenticated)]
    def get(self, request):
        print(request.user)
        user = request.user
        if user.is_staff:
            return Response({"is_admin":True})
        return Response({"is_admin": False})