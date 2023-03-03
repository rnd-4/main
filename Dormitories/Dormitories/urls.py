from django.contrib import admin
from django.urls import path, include
from .views import CorePage

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('hostels.urls')),
    path('', include('users.urls')),
    path('', CorePage, name='mainpage'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
