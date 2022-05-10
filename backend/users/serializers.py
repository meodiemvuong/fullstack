from rest_framework import serializers
from django.core.mail import send_mail

from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'phone', 'email', 'fullName', 'address'  ]
        extra_kwargs = {
            'phone': {'required': False},
            'fullName': {'required': False},
            'address': {'required': False},
            'email': {'required': False},
            'password': {'write_only': True}
        }
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        send = send_mail('Create User', "Hello" + str(self.data['username']), 'thanhbinh16092k1@gmail.com', [self.data['email']]
        , fail_silently=False)
        instance.save()
        return instance