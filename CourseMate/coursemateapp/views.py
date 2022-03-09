from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
# Create your views here.
from .forms import CreateUserForm
from .models import Student, Teacher
from .decorators import unauthenticated_user, teacher_only, student_only

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

@login_required(login_url='coursemateapp:login')
@teacher_only
def teacher(request):
    return render(request, 'teacher.html')

@login_required(login_url='coursemateapp:login')
@student_only
def student(request):
    return render(request, 'student.html')

@unauthenticated_user
def student_register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")

            group = Group.objects.get(name='student')
            user.groups.add(group)
            Student.objects.create(
                user=user, student_ID=username
            )
            messages.success(request, 'Account was created for student' + username)
            return redirect('coursemateapp:login')
    context = {'form': form}
    return render(request, 'register.html', context)

@unauthenticated_user
def teacher_register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")

            group = Group.objects.get(name='teacher')
            user.groups.add(group)
            Teacher.objects.create(
                user=user, teacher_ID=username
            )
            messages.success(request, 'Account was created for teacher' + username)
            return redirect('coursemateapp:login')
    context = {'form': form}
    return render(request, 'register.html', context)

@unauthenticated_user
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group == 'student':
                return redirect('coursemateapp:student')
            if group == 'teacher':
                return redirect('coursemateapp:teacher')
        else:
            messages.info(request, 'Username or password is incorrect')
            return render(request, 'login.html')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('coursemateapp:login')

