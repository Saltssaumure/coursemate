import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'CourseMate.settings')
import django
django.setup()
from django.contrib.auth.models import Group, User
from coursemateapp.models import Student, Teacher, Course, Assignment, Has, Review


def populate():
    group = Group.objects.create(name='teacher')
    group = Group.objects.create(name='student')
    group.save()



    # teacher profiles list
    teachers = [
        {'type': 'teacher', 'name': 'Samuel Goodman', 'username' : 'goodmans', 'email' : 'goodmans@school.com' , 'password' : '3M<IKHSDFkds+tiM!'},
        {'type': 'teacher', 'name': 'Sarah Thompson', 'username' : 'thompsons', 'email' : 'thompsons@school.com' , 'password' : '7L<IKASDKFoer+eiN?'},
        {'type': 'student', 'name': 'Carol Smith', 'username' : 'smithc', 'email' : 'smitchc@school.com' ,'password' : '8MN1vDSFJN183?'},
        {'type': 'student', 'name': 'Jack Davidson', 'username' : 'davidsonj', 'email' : 'davidsonj@school.com' ,'password' : '8WO2qMWOVUN682!'},
    ]

    teacher_id = 1
    student_id = 1
    for person in teachers:
        u = User.objects.create_user(email=person['email'], password=person['password'], username=person['username'])
        if person['type'] == 'teacher':
            print("making a teacher:" + person['name'])
            Teacher.objects.create(user=u, teacher_ID=teacher_id)
        else:
            print("making a student:" + person['name'])
            Student.objects.create(user=u, student_ID=student_id)
        teacher_id += 1
        student_id += 1

if __name__ == '__main__':
    print('Starting coursemateapp population script...')
    populate()