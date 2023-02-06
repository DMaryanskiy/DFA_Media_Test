from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
    
        return token


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("pk", "username", "email", "password",)
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data: dict) -> User:
        user = User.objects.create_user(**validated_data)
        return user


class TokenSerializer(Serializer):
    token = serializers.CharField(max_length=511)
