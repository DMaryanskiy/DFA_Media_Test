import pytest

from django.contrib.auth.models import User
from django.urls import reverse

from fixtures.api_client import api_client, create_user

@pytest.mark.django_db
@pytest.mark.parametrize(
    "username, email, password, status_code", [
        ("NewUser", "foobar@example.com", "1234567890User", 201),
        ("NewUser", "foobarexample.com", "1234567890User", 400),
        ("NewUser", "foobar@example.com", "1234", 400),
        ("", "foobar@example.com", "1234567890User", 400),
        ("NewUser", "", "1234567890User", 201),
        ("NewUser", "foobar@example.com", "", 400),
    ]
)
def test_user_create(api_client, username, email, password, status_code):
    url = reverse("register")
    response = api_client.post(url, {
        "username": username,
        "email": email,
        "password": password,
    })
    assert response.status_code == status_code

@pytest.mark.django_db
@pytest.mark.parametrize(
    "username_create, username_auth, password_create, password_auth, status_code", [
        ("NewUser", "NewUser", "1234567890User", "1234567890User", 200),
        ("NewUser", "AnotherUser", "1234567890User", "1234567890User", 404),
        ("NewUser", "NewUser", "1234567890User", "1234567890NotUser", 404),
    ]
)
def test_login(
    api_client,
    username_create,
    username_auth,
    password_create,
    password_auth,
    status_code
):
    User.objects.create_user(username=username_create, password=password_create)
    url = reverse("login")
    response = api_client.post(url, {
        "username": username_auth,
        "password": password_auth,
    })
    assert response.status_code == status_code

@pytest.mark.django_db
@pytest.mark.parametrize(
    "username, password, need_to_login, status_code", [
        ("NewUser", "1234567890User", True, 200),
        ("NewUser", "1234567890User", False, 404),
    ]
)
def test_user_me(api_client, create_user, username, password, need_to_login, status_code):
    if need_to_login:
        url = reverse("login")
        api_client.post(url, {
            "username": username,
            "password": password,
        })
    url = reverse("get_current_user")
    response = api_client.get(url)
    assert response.status_code == status_code
    if need_to_login:
        assert response.data["user"]["username"] == username
