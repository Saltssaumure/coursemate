from django.test import TestCase, Client
from django.urls import reverse, resolve
from coursemateapp.views import *

from coursemateapp.models import Student, Teacher, Course, Assignment, Has, Review

class IndexViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
    
class AboutViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/coursemateapp/about/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('coursemateapp:about'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('coursemateapp:about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
    


