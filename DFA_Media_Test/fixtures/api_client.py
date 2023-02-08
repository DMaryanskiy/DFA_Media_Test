import pytest

from django.contrib.auth.models import User

@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()

@pytest.fixture
def create_user(username, password):
    User.objects.create_user(username=username, password=password)
