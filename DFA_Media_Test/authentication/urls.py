from django.urls import path

from .views import (
    LoginView,
    UserAPIView,
    UserFromTokenAPIView
)

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("register/", UserAPIView.as_view(), name="register"),
    path("me/", UserFromTokenAPIView.as_view(), name="get_current_user"),
]