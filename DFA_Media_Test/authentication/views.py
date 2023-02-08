from django.contrib.auth import authenticate
from django.conf import settings
from django.middleware import csrf

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import (
    LoginSerializer,
    UserSerializer,
)
from .utils import get_user_by_token

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        data = request.data
        response = Response()        
        username = data.get('username', None)
        password = data.get('password', None)
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                data = get_tokens_for_user(user)
                response.set_cookie(
                    key = settings.SIMPLE_JWT['AUTH_COOKIE'], 
                    value = data["access"],
                    expires = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                    secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                    httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                    samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
                )
                csrf.get_token(request)
                response.data = {"Success" : "Login successfully","data":data}
                return response
            else:
                return Response({"No active" : "This account is not active!!"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"Invalid" : "Invalid username or password!!"}, status=status.HTTP_404_NOT_FOUND)


class UserAPIView(GenericAPIView):
    permission_classes = (AllowAny, )
    serializer_class = UserSerializer

    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data
        }, status=status.HTTP_201_CREATED)


class UserFromTokenAPIView(GenericAPIView):
    permission_classes = (AllowAny, )

    def get(self, request, format=None):
        if self.request.COOKIES.get("access_token"):
            user = get_user_by_token(self.request.COOKIES.get("access_token"))
            return Response({
                "user": UserSerializer(user).data
            })
        return Response({"Invalid" : "You must be logged in!"}, status=status.HTTP_404_NOT_FOUND)
