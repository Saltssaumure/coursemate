from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
# Create your views here.
from .forms import CreateUserForm
from .models import Course, Student, Teacher
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
@teacher_only
def course(request, course_name_slug):
    context_dict = {}
    try:
        course = Course.objects.get(course_name=course_name_slug)
        students = Course.objects.get(students) #Almost definitely wrong need to find another way
        context_dict['course']=course
        context_dict['students'] = students
    except Course.DoesNotExist:
        context_dict['course'] = None
        context_dict['students'] = None
    return render(request, 'course.html', context=context_dict)

@login_required(login_url='coursemateapp:login')
@teacher_only
def regstudent(request):
    return render(request, 'regstudent.html')

@login_required(login_url='coursemateapp:login')
@teacher_only
def editcoursedet(request):
    return render(request, 'editcoursedet.html')

@login_required(login_url='coursemateapp:login')
@teacher_only
def marking(request):
    return render(request, 'marking.html')

@login_required(login_url='coursemateapp:login')
@teacher_only
def editcoursecont(request):
    return render(request, 'editcoursecont.html')

@login_required(login_url='coursemateapp:login')
@teacher_only
def teacherreview(request):
    return render(request, 'teacherreview.html')

@login_required(login_url='coursemateapp:login')
@teacher_only
def regcourse(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            course = form.save()
            ID = form.cleaned_data.get("course_ID")
            name = form.cleaned_data.get("course_name")
            desc = form.cleaned_data.get("course_description")
            group = Group.objects.get(name='course')
            course.groups.add(group)
            Course.objects.create(
                name = name, description=desc
            )
            messages.success(request, 'Course was created for' + name)
            return redirect('coursemateapp:teacher')
    context = {'form': form}
    return render(request, 'regcourse.html')

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
            messages.success(request, 'Account was created for student: ' + username)
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
            messages.success(request, 'Account was created for teacher: ' + username)
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

def upload(request):
    return render(request, 'upload.html')

def writereview(request):
    return render(request, 'writereview.html')

def export(request):
    return render(request, 'export.html')

