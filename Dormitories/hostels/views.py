from django.shortcuts import render

from hostels.models import Hostel, Room
from hostels.enums import RoomTypeChoices
from users.enums import StudentGenderChoices
import random


def create_rooms(request):
    # max_rooms = 44
    # max_floors = 5
    # hostel_id = 4
    #
    # i = 2
    # while i <= max_floors:
    #     floor = i
    #     number = i * 100 + 1
    #     while number <= i * 100 + max_rooms:
    #         price = 600
    #         room_type = RoomTypeChoices.squad_room
    #         gender = StudentGenderChoices.male if number < i * 100 + max_rooms / 2 else StudentGenderChoices.female
    #
    #         room = Room.objects.create(number=number, floor=floor, price=price, room_type=room_type,
    #                                    hostel=Hostel.objects.get(id=hostel_id), gender=gender)
    #         room.room_type = room_type
    #         room.hostel = Hostel.objects.get(id=hostel_id)
    #         room.gender = gender
    #         room.save()
    #
    #         number += 1
    #     i += 1

    return render(request, 'hostels/rooms.html')
