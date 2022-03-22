from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone as timezone
# Create your models here.


class Student(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    student_ID = models.CharField(max_length=8)
    picture = models.ImageField(upload_to='', blank=True)

    def __str__(self):
        return self.student_ID


class Teacher(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    teacher_ID = models.CharField(max_length=8)
    picture = models.ImageField(upload_to='', blank=True)

    def __str__(self):
        return self.teacher_ID


class Course(models.Model):
    teacher = models.ForeignKey(Teacher, null=True, on_delete=models.CASCADE)
    course_ID = models.CharField(max_length=15)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)
    student = models.ManyToManyField(Student)

    def __str__(self):
        return self.course_ID


class Assignment(models.Model):
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Has(models.Model):
    student = models.ForeignKey(Student, null=True, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, null=True, on_delete=models.CASCADE)
    PDF = models.FileField(upload_to='', blank=True)
    Grade = models.FloatField(max_length=10)

    def __str__(self):
        return self.student.student_ID + ' ' + self.assignment.name


class Review(models.Model):
    teacher = models.ForeignKey(Teacher, null=True, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, null=True, on_delete=models.CASCADE)
    review_ID = models.CharField(max_length=15)
    rating = models.FloatField(max_length=10)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.student.student_ID + ' to ' + self.teacher.teacher_ID

