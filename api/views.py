from django.http import JsonResponse
from django.shortcuts import render

def studentsView(request):
  students = {
    'id': 1,
    'name': 'John',
    'class': 'Computer Science',
  }
  
  return JsonResponse(students)
