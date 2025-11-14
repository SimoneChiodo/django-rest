from django.http import JsonResponse
from students.models import Student

def studentsView(request):
  students = Student.objects.all()
  students_list = list(students.values()) # Trasformo gli studenti in un elenco per convertirli in Json
  return JsonResponse(students_list, safe=False) # Uso "safe=False" perché non sto passando un dizionario
