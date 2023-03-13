from django.urls import path
from .views import *

urlpatterns = [
    path('userpage', userPage, name='userpage'),
    path('login', LoginUser.as_view(), name='login'),
    path('register', RegisterUser.as_view(), name='register'),
    path('logout', Logout, name='logout'),
    path('request', statement_request, name='request'),
    path('admin_settlement_requests', admin_statement_requests, name='admin_settlement_requests'),
    path('students', students, name='students'),
    path('rooms/<int:id>', rooms, name='rooms'),
    path('dormitories', dormitories, name='dormitories'),
    path('request_confirm/<int:statement_id>', request_confirm, name='request_confirm'),
    path('accept_request/<int:statement_id>/<int:room_id>/', accept_request, name='accept_request'),
    path('decline-request/<int:id>/', decline_request, name='decline-request'),
]
