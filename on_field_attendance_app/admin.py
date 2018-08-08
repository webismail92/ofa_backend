from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Employee)
admin.site.register(Task)
admin.site.register(AttendanceStatus)
admin.site.register(Status)
admin.site.register(Attendance)

admin.site.site_header = 'On Field Attendance Management System'