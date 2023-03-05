from django.shortcuts import render

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
from django.contrib import messages
from .arrays import regions, facultys


@login_required(login_url='./login')
def userPage(request):
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
    statenebt_request = StatementRequest.objects.filter(user_id=request.user.id).first()
    print(statenebt_request)

    username = request.user.username
    email = request.user.email
    firstname = request.user.first_name
    lastname = request.user.last_name
    location = student.location if student.location else ""
    everage_score = student.everage_score
    faculty = student.faculty
    gender = student.gender
    data = {
        'statement_request': statenebt_request,
        'username': username,
        'firstname': firstname,
        'lastname': lastname,
        'email': email,
        'location': location,
        'gender': gender,
        'faculty': faculty,
        'facultys': facultys,
        'everage_score': everage_score,
        'regions': regions,
    }
    return render(request, 'users/userpage.html', data)


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


def administration(request):
    return render(request, 'users/administration.html')

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
