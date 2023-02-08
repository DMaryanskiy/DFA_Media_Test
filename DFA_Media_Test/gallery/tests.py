import pytest

from django.urls import reverse

@pytest.mark.django_db
def test_get_gallery(api_client):
    url = reverse("gallery_crud-list")
    response = api_client.get(url)
    assert response.status_code == 200
