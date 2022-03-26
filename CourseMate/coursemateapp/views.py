from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
# Create your views here.
from .forms import CreateAssignmentForm, CreateCourseForm, CreateHasForm, AddStudentForm, CreateStudentForm, CreateUserForm, ReviewForm
from .models import Assignment, Course, Has, Review, Student, Teacher
from .decorators import unauthenticated_user, teacher_only, student_only

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

@login_required(login_url='coursemateapp:login')
@teacher_only
def register_course(request):
    form = CreateCourseForm()
    print('1')
    if request.method == 'POST':
        print('2')
        form = CreateCourseForm(request.POST)
        if form.is_valid():
            print('3')
            form.save()
            course_ID = form.cleaned_data.get("course_ID")
            teacher = Teacher.objects.get(user=request.user)
            course = Course.objects.get(course_ID=course_ID)
            course.teacher = teacher
            course.save()
            return redirect('coursemateapp:teacher')
    context = {'form': form}
    return render(request, 'registecourse.html', context)

@login_required(login_url='coursemateapp:login')
@teacher_only
def teacher(request):
    teacher = Teacher.objects.get(teacher_ID=request.user.username)
    course_list = Course.objects.filter(teacher=teacher)
    context_dict = {'courses': course_list}
    return render(request, 'teacher.html', context_dict)

@login_required(login_url='coursemateapp:login')
@teacher_only
def course(request, course_name_slug):
    print("Im in course")
    context_dict = {}
    try:
        course = Course.objects.get(slug=course_name_slug)
        context_dict['course'] = course
    except Course.DoesNotExist:
        context_dict['course'] = None
    return render(request, 'course.html', context_dict)

@login_required(login_url='coursemateapp:login')
@teacher_only
def regstudent(request, course_name_slug):
    course = Course.objects.get(slug=course_name_slug)
    form = AddStudentForm(instance=course)

    if request.method == 'POST':
        form = AddStudentForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('coursemateapp:teacher')
    context = {'form':form}
    return render(request, 'regstudent.html', context)

@login_required(login_url='coursemateapp:login')
@teacher_only
def editcoursedet(request, course_name_slug):
    context_dict = {}
    form = CreateCourseForm()
    if request.method == "POST":
        form = CreateCourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            course_desc = form.cleaned_data.get("description")
            Course.objects.update( #unsure of this
               description = course_desc, course=course_name_slug
            )
            context_dict['course'] = course
            messages.success(request, 'Course desc changed')
    context_dict['form'] =  form
    return render(request, 'editcoursedet.html')

@login_required(login_url='coursemateapp:login')
@teacher_only
def marking(request, course_name_slug):
    context_dict = {}
    try:
        assignment = Assignment.objects.get(course = course_name_slug)
        course = Course.objects.get(course = course_name_slug)
        context_dict["assignments"] = assignment
        context_dict["course"] = course
    except Assignment.DoesNotExist:   
        context_dict["assignments"] = None
        context_dict["course"] = None
    return render(request, 'marking.html', context=context_dict)

@login_required(login_url='coursemateapp:login')
@teacher_only
def markAssign(request, course_name_slug, assignment_name_slug):
    context_dict = {}
    form = CreateHasForm()
    if request.method == "POST":
        form = CreateHasForm(request.POST)
        if form.is_valid():
            has = form.save()
            assign_name = form.cleaned_data.get("assignment_name")
            assign_Grade = form.cleaned_data.get("grade")
            Has.objects.create(
                assignment=assign_name, Grade = assign_Grade, course=course_name_slug
            )
            messages.success(request, 'Assignment was created for course: ' + course_name_slug)
    context_dict['form'] =  form
    try:
        assignment = Assignment.objects.get(course = course_name_slug)
        course = Course.objects.get(course = course_name_slug)
        has = Has.objects.get(assignment = assignment_name_slug)
        context_dict["assignments"] = assignment
        context_dict["course"] = course
        context_dict["has"] = has
    except Assignment.DoesNotExist:  
        context_dict["has"] = None 
        context_dict["assignments"] = None
        context_dict["course"] = None
    return render(request, 'marking.html', context=context_dict)

@login_required(login_url='coursemateapp:login')
@teacher_only
def editcoursecont(request, course_name_slug):
    context_dict = {}
    form = CreateAssignmentForm()
    if request.method == "POST":
        form = CreateAssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save()
            assign_name = form.cleaned_data.get("name")
            assign_desc = form.cleaned_data.get("description")
            Assignment.objects.create(
                name=assign_name, description = assign_desc, course=course_name_slug
            )
            messages.success(request, 'Assignment was created for course: ' + course_name_slug)
    context_dict['form'] =  form
    try:
        assignment = Assignment.objects.get(course = course_name_slug)
        course = Course.objects.get(course = course_name_slug)
        context_dict["assignments"] = assignment
        context_dict["course"] = course
    except Assignment.DoesNotExist:   
        context_dict["assignments"] = None
        context_dict["course"] = None
    return render(request, 'editcoursecont.html', context=context_dict)

@login_required(login_url='coursemateapp:login')
@teacher_only
def teacherreview(request, review_ID_slug):
    context_dict = {}
    try:
        review = Review.objects.get(review_ID = review_ID_slug)
        context_dict['review'] = review
    except Review.DoesNotExist:
        context_dict['review'] = None
    return render(request, 'teacherreview.html', context=context_dict)



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
            user.groups.add(group) #not the right method
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
    form = ReviewForm()
    print('1')
    if request.method == 'POST':
        print('2')
        form = ReviewForm(request.POST)
        if form.is_valid():
            print('3')
            form.save()
            teacher = form.cleaned_data.get("teacher")
            student = Student.objects.get(user=request.user)
            review = Review.objects.get(teacher=teacher, done=False)
            review.student = student
            review.done = True
            review.save()
            return redirect('coursemateapp:student')
    context = {'form': form}
    return render(request, 'writereview.html', context)

def export(request):
    return render(request, 'export.html')

