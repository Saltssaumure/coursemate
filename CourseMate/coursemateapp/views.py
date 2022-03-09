from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def teacher(request):
    return render(request, 'teacher.html')

def student(request):
    return render(request, 'student.html')

def home(request):
    return render(request, 'home.html')

def signup(request):
    return render(request, 'signup.html')

def upload(request):
    return render(request, 'upload.html')