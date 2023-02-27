from django.shortcuts import render
from hostels.models import Hostel


def CorePage(request):
    dormitories = list(Hostel.objects.values())

    data = {
        'dormitories': dormitories,
    }
    return render(request, 'hostels/mainpage.html', data)
