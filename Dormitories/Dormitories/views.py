from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from hostels.models import Hostel
from users.models import Student


def CorePage(request):
    if request.user.is_superuser:
        return HttpResponseRedirect(reverse('admin_settlement_requests'))

    dormitories = list(Hostel.objects.values())

    firstname = ""
    lastname = ""
    gender = ""

    if not request.user.is_anonymous:
        firstname = request.user.first_name
        lastname = request.user.last_name
        student = Student.objects.get(user_id=request.user.id)
        gender = student.gender

    data = {
        'dormitories': dormitories,
        'firstname': firstname,
        'lastname': lastname,
        'gender': gender
    }
    return render(request, 'hostels/mainpage.html', data)
