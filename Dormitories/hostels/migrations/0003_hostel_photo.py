# Generated by Django 4.1.7 on 2023-02-27 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostels', '0002_hostel_information_alter_hostel_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostel',
            name='photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
