from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken

def get_user_by_token(token):
    token = AccessToken(token)
    return get_object_or_404(User, pk=token["user_id"])
