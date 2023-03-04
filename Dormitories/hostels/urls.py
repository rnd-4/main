from django.urls import path
from django.contrib import admin
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dormitorie', dormitoriePage, name='dormitorie'),
]

