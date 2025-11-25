import django_filters
from .models import Employee

class EmployeeFilter(django_filters.FilterSet):
  designation = django_filters.CharFilter(field_name='designation', lookup_expr='iexact') # iexact: il risultato deve essere uguale alla ricerca (specificare una 'lookup_expr' rende il campo Case-Unsensitive)
  emp_name = django_filters.CharFilter(field_name='emp_name', lookup_expr='icontains') # icontains: puù anche solo contenere

  class Meta:
    model = Employee
    fields = ['designation']
