from django.urls import path
from .views import *

urlpatterns = [
    path('dormitorie', dormitoriePage, name='dormitorie'),
]