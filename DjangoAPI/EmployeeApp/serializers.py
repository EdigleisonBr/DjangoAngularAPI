from csv import field_size_limit
from pyexpat import model
from rest_framework import serializers
from EmployeeApp.models import Departments, Employees

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = (
            'department_id',
            'department_name'
        )
    
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = (
            'employee_id',
            'employee_name',
            'department',
            'date_of_joining',
            'photo_file_name'
        )
