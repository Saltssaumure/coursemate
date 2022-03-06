from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello! Welcome to CourseMate! <a href='/coursemateapp/about/'>About</a>")

def about(request):
    return HttpResponse("Here is the About page. <a href='/coursemateapp/'>Index</a>")