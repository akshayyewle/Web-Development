from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Departments_Model, Employees_Model
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer

# Create your views here.
@csrf_exempt
def DepartmentsAPI(request,id=0):
    
    # Read Data
    if request.method == 'GET':
        departments = Departments_Model.objects.all()
        department_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(department_serializer.data, safe=False)
    
    # Create Data
    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data = department_data)
        if department_serializer.is_valid():
            department_serializer.save() # Data Saved To Database
            return JsonResponse("Added Successfully", safe=False)
        else:
            return JsonResponse("Failed to Add",safe=False)

    # Update Data    
    elif request.method =='PUT':
        department_data = JSONParser().parse(request)
        department = Departments_Model.objects.get(DepartmentID = department_data['DepartmentID'])
        department_serializer = DepartmentSerializer(department, data=department_data)
        if department_serializer.is_valid():
            department_serializer.save() # Data Saved To Database
            return JsonResponse("Updated Successfully", safe=False)
        else:
            return JsonResponse("Failed to Update",safe=False)
    
    # Delete Data
    elif request.method == 'DELETE':
        department = Departments_Model.objects.get(DepartmentID=id)
        department.delete() 
        return JsonResponse("Deleted Successfully", safe=False)

# API Methods For Employee Table
@csrf_exempt
def EmployeesAPI(request,id=0):
    if request.method=='GET':
        employees = Employees_Model.objects.all()
        employees_serializer=EmployeeSerializer(employees,many=True)
        return JsonResponse(employees_serializer.data,safe=False)
    elif request.method=='POST':
        employee_data=JSONParser().parse(request)
        employees_serializer=EmployeeSerializer(data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        employee_data=JSONParser().parse(request)
        employee=Employees_Model.objects.get(EmployeeID=employee_data['EmployeeID'])
        employees_serializer=EmployeeSerializer(employee,data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        employee=Employees_Model.objects.get(EmployeeID=id)
        employee.delete()
        return JsonResponse("Deleted Successfully",safe=False)