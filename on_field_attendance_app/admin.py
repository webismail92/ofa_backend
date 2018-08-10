from django.contrib import admin
from .models import *

admin.site.register(Employee)
admin.site.register(Task)
admin.site.register(AttendanceStatus)
admin.site.register(Status)
admin.site.register(Attendance)
# admin.site.register(Place)

admin.site.site_header = 'On Field Attendance Management System'