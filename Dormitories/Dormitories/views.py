from django.shortcuts import render

def CorePage(request):
    render(request, 'hostels/mainpage.html')