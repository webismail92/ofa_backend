from django.conf.urls import url
from django.urls import path, include
from .views import *

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'employee', EmployeeViewSet, 'employee')
router.register(r'task', TaskViewSet, 'task')
router.register(r'attendance', AttendanceViewSet, 'attendance')

urlpatterns = [
    path('login/',  Login.as_view(), name = 'Login'),
    path('', include(router.urls)),
]