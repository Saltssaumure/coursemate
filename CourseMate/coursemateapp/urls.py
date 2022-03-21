from django.urls import path
from coursemateapp import views

app_name = 'coursemateapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('student/', views.student, name='student'),
    path('student/upload-assessment', views.upload, name="upload"),
    path('student/write-review', views.writereview, name="writereview"),
    path('student/export-grade', views.export, name="export"),
    path('teacher/', views.teacher, name='teacher'),
    path('teacher/<slug:course_name_slug>', views.course, name='course'), #test
    path('teacher/<slug:course_name_slug>/register-student', views.regstudent, name='regstudent'), #implement
    path('teacher/<slug:course_name_slug>/edit-course-detail', views.editcoursedet, name='editcoursedet'), #implement
    path('teacher/<slug:course_name_slug>/marking', views.marking, name='marking'), #implement
    path('teacher/<slug:course_name_slug>/edit-course-cont', views.editcoursecont, name='editcoursecont'), #implement
    path('teacher/review', views.teacherreview, name='teacherreview'),  #implement
    path('teacher/register-course', views.regcourse, name='regcourse'), #test
    path('login/', views.loginpage, name='login'),
    path('student-register/', views.student_register, name='student-register'),
    path('teacher-register/', views.teacher_register, name='teacher-register'),
    path('logout/', views.user_logout, name='logout'),
]