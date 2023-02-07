from rest_framework import serializers

from .models import Gallery


class GallerySerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source="creator.username")
    image_url = serializers.ImageField(required=True)

    class Meta:
        model = Gallery
        fields = "__all__"
