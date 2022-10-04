
# Imports
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

ADMIN_URL = [
    path('admin/', admin.site.urls),
]
APPLICATION_URLS = [
    path('', include('revwand.urls')),
    path('', include('revwizard.urls')),
]
EXTERNAL_URLS = []
STATIC_URLS = []
STATIC_URLS += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


urlpatterns = ADMIN_URL + APPLICATION_URLS + EXTERNAL_URLS + STATIC_URLS
