from django.urls import path
from .views import *

urlpatterns = [
    path('rooms', create_rooms),
]

