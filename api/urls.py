from django.urls import path
from . import views

urlpatterns = [
    # Students
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentDetailView),

    # Employees
    path('employees/', views.Employees.as_view()),
    path('employees/<int:pk>/', views.EmployeeDetail.as_view()),
]
