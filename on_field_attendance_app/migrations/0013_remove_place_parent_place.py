# Generated by Django 2.0.2 on 2018-08-10 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('on_field_attendance_app', '0012_place_parent_place'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='parent_place',
        ),
    ]
