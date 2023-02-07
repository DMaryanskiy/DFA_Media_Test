from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/users/", include("authentication.urls")),
    path("api/v1/gallery/", include("gallery.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
