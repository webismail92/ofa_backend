from django.db import models
import jwt
from location_field.models.plain import PlainLocationField

# modules for auth
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)

# Create your models here.
class Status(models.Model):
    status = models.CharField(max_length=100)
    def __str__(self):
        return self.status

class AttendanceStatus(models.Model):
    status = models.CharField(max_length=100)
    def __str__(self):
        return self.status

class Employee(models.Model):
    profile_pic = models.ImageField(upload_to = '', default = 'None/no-img.jpg')
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=30,blank=True)
    state = models.CharField(max_length=30,blank=True)
    mobile_no = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Task(models.Model):
    assignedTo = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=False)
    description = models.CharField(max_length=100)
    title = models.CharField(max_length=100, null=True, blank=True)
    comment = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    address = PlainLocationField(based_fields=['city'], zoom=7,null=True, blank=True)
    location = PlainLocationField(based_fields=['city'], zoom=7,null=True, blank=True)
    def __str__(self):
        return self.title

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False)
    attendance = models.ForeignKey(AttendanceStatus, on_delete=models.CASCADE, null=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    def __str__(self):
        return self.employee + ' ' + self.attendance

class Place(models.Model):
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7)