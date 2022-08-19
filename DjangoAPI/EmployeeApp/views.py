from email.policy import default
from typing_extensions import Required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Departments, Employees
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def department_api(request, id=0):
    if request.method == 'GET':
        departments = Departments.objects.all().order_by('department_name')
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False) # search :: safe=False
    
    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)
    
    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(department_id = department_data['department_id'])
        department_serializer = DepartmentSerializer(department, data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    
    elif request.method == 'DELETE':
        print(id)
        department = Departments.objects.get(department_id=id)
        department.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)


@csrf_exempt
def employee_api(request, id=0):
    if request.method == 'GET':
        employees = Employees.objects.all()
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False) # search :: safe=False
    
    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data)
        print(employee_serializer)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)
    
    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Employees.objects.get(employee_id = employee_data['employee_id'])
        employee_serializer = EmployeeSerializer(employee, data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            # return JsonResponse(employee_serializer.data, safe=False)
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    
    elif request.method == 'DELETE':
        employee = Employees.objects.get(employee_id = id)
        employee.delete()
        return JsonResponse("Deletd Successfully!!", safe=False)


@csrf_exempt
def save_file(request):
    file = request.FILES['uploaded_file']
    file_name = default_storage.save(file.name, file)
    
    return JsonResponse(file_name, safe=False)