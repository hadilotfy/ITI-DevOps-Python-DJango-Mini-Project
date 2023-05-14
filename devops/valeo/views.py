from django.shortcuts import render
from valeo.models import Employee
# Create your views here.

def index(request):
    employees = Employee.objects.all()
    return render(request, 'index.html' , context={'employees': employees})

