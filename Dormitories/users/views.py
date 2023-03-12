from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout

from .forms import LoginUserForm, RegisterUserForm
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .models import Student, StatementRequest
from hostels.models import Hostel, Room
from django.contrib import messages
from .arrays import *
from .enums import *


@login_required(login_url='./login')
def userPage(request):
    if request.user.is_superuser:
        return HttpResponseRedirect(reverse('admin_settlement_requests'))

    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        faculty = request.POST['faculty']
        gender = request.POST['gender']
        location = request.POST['location']
        everage_score = request.POST['everage_score']

        username = request.user.username
        user = User.objects.get(username=username)
        user_id = request.user.id

        student = Student.objects.get(user_id=user_id)
        if not student:
            Student.objects.create(gender=gender, faculty=faculty, user_id=user_id)
        else:
            student.gender = gender
            student.faculty = faculty
            student.location = location
            student.everage_score = everage_score
            student.save()

        user.first_name = firstname
        user.last_name = lastname
        user.save()
        return HttpResponseRedirect(reverse('userpage'))

    student = Student.objects.get(user_id=request.user.id)
    students = Student.objects.filter(room=student.room)
    statenebt_request = StatementRequest.objects.filter(user_id=request.user.id).first()
    if student.room:
        dormitory = Hostel.objects.get(id=student.room.hostel.id)
    else:
        dormitory = None

    username = request.user.username
    email = request.user.email
    firstname = request.user.first_name
    lastname = request.user.last_name
    location = student.location if student.location else ""
    everage_score = student.everage_score
    gender = student.gender
    faculty = student.faculty
    room = student.room if student.room else None
    payment_status = student.payment_status

    data = {
        'statement_request': statenebt_request,
        'dormitory': dormitory,
        'students': students,

        'username': username,
        'firstname': firstname,
        'lastname': lastname,
        'email': email,
        'location': location,
        'gender': gender,
        'faculty': faculty,
        'room': room,
        'payment_status': payment_status,

        'genders': StudentGenderChoices,
        'facultys': facultys,
        'everage_score': everage_score,
        'regions': regions,
    }
    return render(request, 'users/userpage.html', data)


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('userpage')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')


def UserLoggedIn(request):
    if request.user.is_authenticated == True:
        username = request.user.username
    else:
        username = None
    return username


def Logout(request):
    username = UserLoggedIn(request)
    if username != None:
        logout(request)
        url_match = reverse_lazy('mainpage')
        return redirect(url_match)


def statement_request(request):
    student = Student.objects.get(user_id=request.user.id)

    email = request.user.email
    firstname = request.user.first_name
    lastname = request.user.last_name
    location = student.location if student.location else ""
    gender = student.gender
    everage_score = student.everage_score
    faculty = student.faculty

    if (not email or not firstname or not lastname or not location or not gender or not everage_score or not faculty):
        positions = []
        if not email:
            positions.append("email")
        if not firstname:
            positions.append("firstname")
        if not lastname:
            positions.append("lastname")
        if not location:
            positions.append("location")
        if not gender:
            positions.append("gender")
        if not everage_score:
            positions.append("everage_score")
        if not faculty:
            positions.append("faculty")

        message = "Yor data is not complete please fill the next positions:"
        for position in positions:
            if position != positions[len(positions) - 1]:
                message += " " + position + ","
            else:
                message += " " + position + "."

        messages.add_message(request, messages.WARNING, message)
        return HttpResponseRedirect(reverse('userpage'))
    else:
        statement_request = StatementRequest.objects.create(user_id=request.user.id)
        statement_request.save()
        return HttpResponseRedirect(reverse('userpage'))


def admin_statement_requests(request):
    statement_requests = StatementRequest.objects.filter()

    information = list()
    for settlement in statement_requests:
        if not settlement.approved:
            user = User.objects.get(id=settlement.user.id)
            student = Student.objects.get(user_id=user.id)
            information.append({
                'user': user,
                'student': student,
                'statement': settlement,
            })

    data = {
        'information': information,
    }
    return render(request, 'users/admin_settlement_requests.html', data)


def request_confirm(request, statement_id):
    statement = StatementRequest.objects.get(id=statement_id)
    student = Student.objects.get(user_id=statement.user_id)

    hostels = Hostel.objects.all()
    hostels_data = []

    for hostel in hostels:
        rooms = Room.objects.filter(hostel=hostel).order_by('floor', 'number')
        rooms_data = []

        for room in rooms:
            number_of_residents = Student.objects.filter(room=room).count()

            id = room.id
            number = room.number
            floor = room.floor
            price = room.price
            room_type = room.room_type
            gender = room.gender

            rooms_data.append({
                'id': id,
                'number': number,
                'floor': floor,
                'price': price,
                'room_type': room_type,
                'gender': gender,

                'number_of_residents': number_of_residents,
            })

        hostels_data.append({
            'hostel': hostel,
            'rooms': rooms_data,
        })

    data = {
        'hostels_data': hostels_data,
        'statement': statement,
        'student': student,
        'genders': StudentGenderChoices,
    }

    return render(request, 'users/request_confirm.html', data)


def students(request):
    students = Student.objects.filter()

    info = list()
    for student in students:
        user = User.objects.get(id=student.user.id)
        info.append({
            'user': user,
            'student': student,
        })

    data = {
        'information': info,
    }
    return render(request, 'users/students.html', data)


def rooms(request, id):
    room = Room.objects.get(id=id)
    hostel = Hostel.objects.get(id=room.hostel.id)
    students = Student.objects.filter(room=room)
    number_of_rooms = Room.objects.filter(hostel=hostel).count()


    data = {
        'room': room,
        'dormitory': hostel,
        'students': students,
        'number_of_rooms': number_of_rooms,
    }
    return render(request, 'users/room.html', data)


def dormitories(request):
    hostels = Hostel.objects.all()
    hostels_data = []

    for hostel in hostels:
        rooms = Room.objects.filter(hostel=hostel).order_by('floor', 'number')
        rooms_data = []

        for room in rooms:
            number_of_residents = Student.objects.filter(room=room).count()

            id = room.id
            number = room.number
            floor = room.floor
            price = room.price
            room_type = room.room_type
            gender = room.gender

            rooms_data.append({
                'id': id,
                'number': number,
                'floor': floor,
                'price': price,
                'room_type': room_type,
                'gender': gender,

                'number_of_residents': number_of_residents,
            })

        hostels_data.append({
            'hostel': hostel,
            'rooms': rooms_data,
        })

    data = {
        'hostels_data': hostels_data,
        'genders': StudentGenderChoices,
    }
    return render(request, 'users/dormitories.html', data)


def accept_request(request, statement_id, room_id):
    statement = StatementRequest.objects.get(id=statement_id)
    room = Room.objects.get(id=room_id)
    student = Student.objects.get(user_id=statement.user.id)

    student.room = room
    student.save()

    statement.approved = True
    statement.save()
    return HttpResponseRedirect(reverse('admin_settlement_requests'))


def decline_request(request, id):
    statement = StatementRequest.objects.get(id=id)
    statement.delete()
    return HttpResponseRedirect(reverse('admin_settlement_requests'))
