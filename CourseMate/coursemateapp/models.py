from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    student_ID = models.CharField(max_length=8)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.student_ID

class Teacher(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    teacher_ID = models.CharField(max_length=8)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.teacher_ID
