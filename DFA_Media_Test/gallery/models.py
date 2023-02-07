from django.contrib.auth.models import User
from django.db import models

def upload_to(instance, filename):
    return f"images/{filename}"


class Gallery(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="gallery_user")
    title = models.CharField(max_length=80, blank=False, null=False)
    image_url = models.ImageField(upload_to=upload_to, blank=False, null=False)
