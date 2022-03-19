from django.test import TestCase, Client, RequestFactory
from django.urls import reverse, resolve
from coursemateapp.views import *
from django.contrib.auth.models import User, Permission, AnonymousUser


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
    
class TeacherRegisterView(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/coursemateapp/teacher-register/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('coursemateapp:teacher-register'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('coursemateapp:teacher-register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

class StudentRegisterView(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/coursemateapp/student-register/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('coursemateapp:student-register'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('coursemateapp:student-register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

class StudentViewTest(TestCase):

    def setUp(self):
        # create two students 
        test_user1 = User.objects.create_user(username='student1', password='3M<IKHSDFkds+tiM!')
        test_user2 = User.objects.create_user(username='student2', password='8MN1vDSFJN183?')

        test_user1.save()
        test_user2.save()

    def test__for_login_restriction_permission_and_template(self):
        # try to call the Restricted View as Anonymous
        response = self.client.get(reverse('coursemateapp:student'))
        # check for Login Prompt Redirection
        self.assertRedirects(response, '/coursemateapp/login/?next=/coursemateapp/student/')
        self.user = User.objects.get(username="student1")
        # login with the Client
        login = self.client.login(username='student1', password='3M<IKHSDFkds+tiM!')
        # check user is logged in
        self.assertTrue(login)
        # check for username
        self.assertEqual(self.user.username, 'student1')
        # call the Restricted View as logged in User again but without Permission
        # response = self.client.get(reverse('coursemateapp:student'))
        # # Check for HTTPResponseForbidden
        # self.assertEqual(response.status_code, 403)
    
    
    
    


