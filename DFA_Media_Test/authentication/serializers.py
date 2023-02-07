from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer


class LoginSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("pk", "username", "password")
        extra_kwargs = {"password": {"write_only": True}}


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("pk", "username", "email", "password",)
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data: dict) -> User:
        user = User.objects.create_user(**validated_data)
        return user
