from django.db import models
from .enums import RoomTypeChoices
from users.enums import StudentGenderChoices


class Hostel(models.Model):
    name = models.CharField(max_length=16)
    email = models.EmailField()
    phone = models.CharField(max_length=18)
    location = models.URLField()
    information = models.TextField(null=True)
    photo = models.ImageField(null=True, upload_to="images/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Hostel'
        verbose_name_plural = 'Hostels'


class Room(models.Model):
    hostel = models.ForeignKey(to=Hostel, on_delete=models.CASCADE)
    number = models.IntegerField()
    floor = models.IntegerField()
    price = models.IntegerField()
    room_type = models.CharField(max_length=13, choices=RoomTypeChoices.choices)
    gender = models.CharField(max_length=13, choices=StudentGenderChoices.choices, default=StudentGenderChoices.male)

    def __str__(self):
        return str(self.number)

    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'
