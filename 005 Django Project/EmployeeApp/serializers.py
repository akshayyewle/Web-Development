from rest_framework import serializers
from EmployeeApp.models import Departments_Model, Employees_Model

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments_Model
        fields = ('DepartmentID', 'DepartmentName')
    
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees_Model
        fields = ('EmployeeID', 'EmployeeName', 'Department', 'DateOfJoining', 'PhotoFileName')