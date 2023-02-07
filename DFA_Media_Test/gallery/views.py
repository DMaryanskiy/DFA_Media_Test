from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .models import Gallery
from .serializers import GallerySerializer

from authentication.utils import get_user_by_token


class GalleryViewSet(ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

    def perform_create(self, serializer):
        user = get_user_by_token(self.request.COOKIES.get("access_token"))
        serializer.save(creator=user)


class GalleryDelete(GenericAPIView):
    permission_classes = (IsAdminUser, )
    def delete(self, request):
        Gallery.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
