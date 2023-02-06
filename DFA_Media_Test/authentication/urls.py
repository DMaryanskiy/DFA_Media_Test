from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    MyTokenObtainPairView,
    UserAPIView,
    UserFromTokenAPIView
)

urlpatterns = [
    path("token/", MyTokenObtainPairView.as_view(), name="token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", UserAPIView.as_view(), name="register"),
    path("me/", UserFromTokenAPIView.as_view(), name="get_current_user"),
]