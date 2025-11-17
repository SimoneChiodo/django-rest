from django.http import JsonResponse
from students.models import Student
from .serializers import StudentSerializer, EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employees.models import Employee

# STUDENTS -------------------------
# def studentsView(request):
#   students = Student.objects.all()
#   students_list = list(students.values()) # Trasformo gli studenti in un elenco per convertirli in Json
#   return JsonResponse(students_list, safe=False) # Uso "safe=False" perché non sto passando un dizionario

@api_view(['GET', 'POST'])
def studentsView(request):
  if request.method == 'GET': # GET -----
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True) # Serializzo gli studenti (many=True è perché passo più di uno studente in una volta)
    return Response(serializer.data, status=status.HTTP_200_OK) 
  elif request.method == 'POST': # POST -----
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid(): # Controllo i dati
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # Se i dati sono sbagliati


@api_view(['GET', 'PUT', 'DELETE'])
def studentDetailView(request, pk):
  try:
    student = Student.objects.get(pk=pk)
  except Student.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  
  if request.method == 'GET': 
    serializer = StudentSerializer(student) 
    return Response(serializer.data, status=status.HTTP_200_OK) 
  elif request.method == 'PUT': 
    serializer = StudentSerializer(student, data=request.data) # Imposto lo studente specifico
    if serializer.is_valid(): # Controllo la validità dei dati
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK) 
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # Se i dati sono sbagliati
  elif request.method == 'DELETE': 
    student.delete()
    return Response(status=status.HTTP_204_NO_CONTENT) 

# EMPLOYEES -------------------------
class Employees(APIView):
  # INDEX
  def get(self, request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  # CREATE
  def post(self, request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)
