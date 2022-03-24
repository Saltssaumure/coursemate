from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Assignment, Student, Teacher, Course


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']

class CreateCourseForm(UserCreationForm):
    class Meta:
        model = Course 
        fields = ['course_ID', 'name', 'description']

class CreateAssignmentForm(UserCreationForm):
    class Meta:
        model = Assignment 
        fields = ['name', 'course', 'description', 'student']

class CreateHasForm(UserCreationForm):
    class Meta:
        model = Assignment 
        fields = ['assignment', 'Grade']
        