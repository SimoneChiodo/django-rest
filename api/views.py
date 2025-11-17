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

@api_view(['GET'])
def studentsView(request):
  if request.method == 'GET':
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True) # Serializzo gli studenti (many=True è perché passo più di uno studente in una volta)
    return Response(serializer.data, status=status.HTTP_200_OK) # Uso "safe=False" perché non sto passando un dizionario
