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
    path('home/', views.home, name='home'),
    path('sign-up/', views.signup, name='signup'),
]