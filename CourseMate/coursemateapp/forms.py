from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Assignment, Has, Student, Teacher, Course, Review


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']

class CreateStudentForm(UserCreationForm):
    class Meta:
        model = Student 
        fields = ['student_ID']


class CreateCourseForm(ModelForm):
    class Meta:
        model = Course 
        fields = ['course_ID', 'name', 'description']

class CreateAssignmentForm(UserCreationForm):
    class Meta:
        model = Assignment 
        fields = ['name', 'course', 'description', 'student']

class CreateHasForm(UserCreationForm):
    class Meta:
        model = Has 
        fields = ['assignment', 'Grade']

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['teacher', 'rating', 'description']

class AddStudentForm(ModelForm):
    class Meta:
        model = Course
        fields = ['student']
