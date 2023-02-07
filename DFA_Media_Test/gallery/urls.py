from django.urls import path
from rest_framework import routers

from .views import GalleryViewSet, GalleryDelete

router = routers.DefaultRouter()
router.register(r"", GalleryViewSet)

urlpatterns = [
    path("delete/all/", GalleryDelete.as_view(), name="delete_all"),
]

urlpatterns += router.urls
