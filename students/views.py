from django.http import HttpResponse
from django.shortcuts import render

def students(request):
  
  return HttpResponse('<h2>Hello World</h2>')
