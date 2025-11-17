from django.http import JsonResponse
from students.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

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


@api_view(['GET'])
def studentDetailView(request, pk):
  try:
    student = Student.objects.get(pk=pk)
  except Student.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  
  if request.method == 'GET': 
    serializer = StudentSerializer(student) 
    return Response(serializer.data, status=status.HTTP_200_OK) 
