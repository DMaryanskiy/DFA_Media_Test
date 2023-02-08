from django.core import exceptions
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("pk", "username", "password")
        extra_kwargs = {"password": {"write_only": True}}


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("pk", "username", "email", "password",)
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data: dict) -> User:
        user = User.objects.create_user(**validated_data)
        return user
    
    def validate(self, data):
        user = User(**data)
        password = data.get("password")
        errors = dict()
        try:
            validate_password(password, user)
        except exceptions.ValidationError as e:
            errors["password"] = list(e.messages)
        
        if errors:
            raise serializers.ValidationError(errors)
        
        return super(UserSerializer, self).validate(data)
