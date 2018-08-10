from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from django.http import HttpResponse, JsonResponse, HttpRequest
import json
from django.views.decorators.csrf import csrf_exempt
from .filters import *
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint for login"""
    filter_class = EmployeeFilters
    serializer_class = EmployeeSrializer
    queryset = Employee.objects.all()

class AttendanceViewSet(viewsets.ModelViewSet):
    """
    API endpoint for login"""
    filter_class = AttendanceFilters
    serializer_class = AttendanceSrializer
    queryset = Attendance.objects.all()

class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint for login"""
    filter_class = TaskFilters
    serializer_class = TaskSrializer
    queryset = Task.objects.all()

class Login(APIView):
    def get_object_by_username(self, username, password):
        try:
            return Employee.objects.filter(username=username, password = password)
        except ObjectDoesNotExist:
            raise Http404
    def post(self, request, format = None):
        print('data', request.data)
        username = request.data.get('username')
        password = request.data.get('password')
        print('username', username)
        if username and password : 
            employee = self.get_object_by_username(request.data.get('username'), request.data.get('password'))
            serializer = UserSerializer(employee, many = True)
            if employee.exists():
                return Response({"data":serializer.data[0],"status":200} , status = status.HTTP_200_OK)
            return Response( {"success":False,"message": "You are not register with us", "status":401},status=status.HTTP_400_BAD_REQUEST)
        return Response( {"success":False,"message": "user name or password missing","status":401}, status=status.HTTP_400_BAD_REQUEST)