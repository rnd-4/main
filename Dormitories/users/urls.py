from django.urls import path
from .views import *

urlpatterns = [
    path('userpage', userPage, name='userpage'),
    path('login', LoginUser.as_view(), name='login'),
    path('register', RegisterUser.as_view(), name='register'),
    path('logout', Logout, name='logout'),
    path('request', statement_request, name='request'),
    path('admin_settlement_requests', admin_settlement_requests, name='admin_settlement_requests'),
    path('students', students, name='students')
]
