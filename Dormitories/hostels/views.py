from django.shortcuts import render
from users.models import Student
from django.contrib.auth.models import User
from .models import Hostel, Room


def dormitoriePage(request):
    if request.user.is_authenticated == True:
        user_id = request.user.id
        student = Student.objects.get(user_id=user_id)

        if (student == 'Kyiv'):
            return render(request, 'hostels/sorry.html')
        elif (student.room != None):
            room = Room.objects.get(id=student.room.id)
            dormitorie = Hostel.objects.get(id=room.hostel_id)
            students = list(Student.objects.filter(room=room))
            #
            # users=list()
            # for student in students:
            #
            #     user = User.objects.get(id=student.user.id)
            #     print(user)
            #     user_data={
            #         'firstname': user.first_name,
            #         'lastname': user.last_name,
            #         'email': user.email,
            #         'faculty': student.faculty,
            #         'gender': student.gender,
            #     }
            #     users.__add__(user_data)
            #     print(user_data)

            floor = room.floor
            number = room.number
            payment_status = student.payment_status
            data = {
                'dormitorie': dormitorie,
                'floor': floor,
                'number': number,
                'payment_status': payment_status,
                'students': students,
            }
            print(data)

            return render(request, 'hostels/dormitorie.html', data)
        else:
            return render(request, 'hostels/register.html')
    else:
        return render(request, 'users/login.html')
