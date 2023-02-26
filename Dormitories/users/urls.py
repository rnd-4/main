from django.urls import path
from .views import *

urlpatterns = [
    path('userpage', userPage, name='userpage'),
    path('login', LoginUser.as_view(), name='login'),
    path('register', RegisterUser.as_view(), name='register'),
    path('logout', Logout, name='logout'),
]