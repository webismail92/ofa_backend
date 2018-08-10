from on_field_attendance_app.models import *
from rest_framework import serializers

class EmployeeSrializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
        
class AttendanceSrializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"

class TaskSrializer(serializers.ModelSerializer):
    details = serializers.SerializerMethodField()
    class Meta:
        model = Task
        fields = "__all__"

    def get_details(self, obj):
        request = self.context.get('request')
        employeepic = request.build_absolute_uri(obj.assignedTo.profile_pic.url)
        print('url ', employeepic)
        return {
            "assignedTo": {
                "pk": obj.assignedTo.pk, 
                "username": obj.assignedTo.username,
                "first_name": obj.assignedTo.first_name,
                "last_name": obj.assignedTo.last_name,
                "profile_pic": employeepic,
                "city": obj.assignedTo.city,
                "state": obj.assignedTo.state,
                "mobile_no": obj.assignedTo.mobile_no,
                "email": obj.assignedTo.email,
                "designation": obj.assignedTo.designation
            },
            "status": {"pk": obj.status.pk, "status": obj.status.status}
        }
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'    
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'