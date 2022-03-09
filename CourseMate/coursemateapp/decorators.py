from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('coursemateapp:student')

        return view_func(request, *args, **kwargs)
    return wrapper_func

def teacher_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'student':
            return redirect('coursemateapp:student')
        if group == 'teacher':
            return view_func(request, *args, **kwargs)
    return wrapper_func

def student_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'teacher':
            return redirect('coursemateapp:teacher')
        if group == 'student':
            return view_func(request, *args, **kwargs)
    return wrapper_func
