from django.contrib import admin
from .models import Student, Teacher, Course, Assignment, Has, Review
# Register your models here.

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Assignment)
admin.site.register(Has)
admin.site.register(Review)
