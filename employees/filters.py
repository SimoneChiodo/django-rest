import django_filters
from .models import Employee

class EmployeeFilter(django_filters.FilterSet):
  designation = django_filters.CharFilter(field_name='designation', lookup_expr='iexact') # iexact: lo rende Case-Unsensitive

  class Meta:
    model = Employee
    fields = ['designation']
