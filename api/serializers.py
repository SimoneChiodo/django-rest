from rest_framework import serializers
from students.models import Student
from employees.models import Employee

class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = "__all__" # Seleziono tutti i campi dello studente

class EmployeeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Employee
    fields = "__all__"
