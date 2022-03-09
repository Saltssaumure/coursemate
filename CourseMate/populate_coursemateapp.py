import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'CourseMate.settings')
import django
django.setup()
from django.contrib.auth.models import Group

def populate():
    group = Group.objects.create(name='teacher')
    group = Group.objects.create(name='student')
    group.save()


if __name__ == '__main__':
    print('Starting coursemateapp population script...')
    populate()
