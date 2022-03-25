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
    path('teacher/<slug:course_name_slug>', views.course, name='course'),
    path('teacher/<slug:course_name_slug>/register-student', views.regstudent, name='regstudent'), #implement html properly, check views
    path('teacher/<slug:course_name_slug>/edit-course-detail', views.editcoursedet, name='editcoursedet'), #test, check views
    path('teacher/<slug:course_name_slug>/marking', views.marking, name='marking'), #test
    path('teacher/<slug:course_name_slug>/marking/<slug:assignment_name_slug>', views.markAssign, name='markAssign'), #do html check view logic
    path('teacher/<slug:course_name_slug>/edit-course-cont', views.editcoursecont, name='editcoursecont'), #test
    path('teacher/review/<slug:review_ID_slug>', views.teacherreview, name='teacherreview'),  #test, fix models
    path('register-course/', views.register_course, name='register-course'), #test, fix field Error
    path('login/', views.loginpage, name='login'),
    path('student-register/', views.student_register, name='student-register'),
    path('teacher-register/', views.teacher_register, name='teacher-register'),
    path('logout/', views.user_logout, name='logout'),
]