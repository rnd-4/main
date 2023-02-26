from django.contrib import admin
from django.urls import path, include
from .views import CorePage

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('hostels.urls')),
    path('', include('users.urls')),
    path('', CorePage, name='mainpage'),
]
