from django.shortcuts import render

def CorePage(request):
    return render(request, 'hostels/mainpage.html')