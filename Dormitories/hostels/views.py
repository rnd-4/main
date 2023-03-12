from django.contrib.auth.models import User
from django.shortcuts import render

from hostels.models import Hostel, Room
from hostels.enums import RoomTypeChoices
from users.enums import *
from users.arrays import *
import random

from users.models import Student


def go(request):
    return render(request, 'hostels/rooms.html')


def room_creator():
    max_rooms = 44
    max_floors = 5
    hostel_id = 4

    i = 2
    while i <= max_floors:
        floor = i
        number = i * 100 + 1
        while number <= i * 100 + max_rooms:
            price = 600
            room_type = RoomTypeChoices.squad_room
            gender = StudentGenderChoices.male if number < i * 100 + max_rooms / 2 else StudentGenderChoices.female

            room = Room.objects.create(number=number, floor=floor, price=price, room_type=room_type,
                                       hostel=Hostel.objects.get(id=hostel_id), gender=gender)
            room.room_type = room_type
            room.hostel = Hostel.objects.get(id=hostel_id)
            room.gender = gender
            room.save()

            number += 1
        i += 1


def student_creator(max_students, faculty):
    female_first_names = open('hostels/templates/female_first_name.txt', 'r', encoding="utf8").read().splitlines()
    male_first_names = open('hostels/templates/male_first_name.txt', 'r', encoding="utf8").read().splitlines()
    last_names = open('hostels/templates/last_name.txt', 'r', encoding="utf8").read().splitlines()

    i = 0
    while i < max_students:
        login = student_id()
        pasword = "password" + login
        email = login + "@stud.nau.edu.ua"
        average_score = random.randint(65, 100)
        gender = random.choice([StudentGenderChoices.male, StudentGenderChoices.female])
        first_name = random.choice(male_first_names) if gender == StudentGenderChoices.male else random.choice(
            female_first_names)
        last_name = random.choice(last_names)
        region = random.choice(regions)

        user = User.objects.create(password=pasword, username=login, first_name=first_name, last_name=last_name,
                                   email=email)
        user.set_password(pasword)
        user.save()

        student = Student.objects.create(user=user, faculty=faculty, everage_score=average_score, gender=gender,
                                         location=region)
        i += 1


def student_id():
    login = random.randint(10000000, 99999999)

    i = 0
    l = login
    while l / 10 > 0:
        l = l / 10
        i += 1

    i = 8 - i
    while i > 0:
        login = '0' + str(login)
        i -= 1

    if User.objects.filter(username=login).exists():
        return student_id()
    else:
        return str(login)


def settlement(count, faculty, hostel_id):
    students = Student.objects.filter(faculty=faculty).order_by('everage_score')

    hostel = Hostel.objects.get(id=hostel_id)
    rooms = Room.objects.filter(hostel=hostel)

    i = 0
    for student in students:
        student.room = random.choice(rooms)
        student.save()
        i += 1
        if i >= count:
            break


def choiceRoom(hostel, gender):
    hostel = Hostel.objects.get(id=hostel)
    rooms = Room.objects.filter(hostel=hostel, gender=gender)
    room = random.choice(rooms)

    if Student.objects.filter(room=room).count() >= 4:
        return choiceRoom(hostel, gender)
    else:
        return room
