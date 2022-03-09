from django.urls import path
from coursemateapp import views

app_name = 'coursemateapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('teacher/', views.teacher, name='teacher'),
    path('student/', views.student, name='student'),
    path('student/upload-assessment', views.upload, name="upload"),
    path('student/write-review', views.writereview, name="writereview"),
    path('student/export-grade', views.export, name="export"),
    path('login/', views.loginpage, name='login'),
    path('student-register/', views.student_register, name='student-register'),
    path('teacher-register/', views.teacher_register, name='teacher-register'),
    path('logout/', views.user_logout, name='logout'),
]