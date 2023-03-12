from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from hostels.models import Hostel


def CorePage(request):
    if request.user.is_superuser:
        return HttpResponseRedirect(reverse('admin_settlement_requests'))

    dormitories = list(Hostel.objects.values())

    data = {
        'dormitories': dormitories,
    }
    return render(request, 'hostels/mainpage.html', data)
