# Generated by Django 4.1.7 on 2023-03-03 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='room_id',
            new_name='room',
        ),
    ]