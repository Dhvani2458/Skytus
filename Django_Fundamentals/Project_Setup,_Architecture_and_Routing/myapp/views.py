from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to Django!")


def student_detail(request, student_id):
    return HttpResponse(f"Student ID: {student_id}")