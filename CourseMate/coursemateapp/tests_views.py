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
    
class TeacherRegisterViewTest(TestCase):

    def setUp(self):
        # create two teachers 
        test_user1 = User.objects.create_user(username='teacher1', password='3M<IKHSDFkds+tiM!')
        test_user2 = User.objects.create_user(username='teacher2', password='8MN1vDSFJN183?')

        test_user1.save()
        test_user2.save()

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
    
    def test__for_login_restriction_permission_and_template(self):
        # try to call the Restricted View as Anonymous
        response = self.client.get(reverse('coursemateapp:teacher'))
        # check for Login Prompt Redirection
        self.assertRedirects(response, '/coursemateapp/login/?next=/coursemateapp/teacher/')
        self.user = User.objects.get(username="teacher1")
        # login with the Client
        login = self.client.login(username='teacher`', password='wrong')
        # check user can't login with wrong password
        self.assertFalse(login)
        login = self.client.login(username='teacher1', password='3M<IKHSDFkds+tiM!')
        # check user is logged in
        self.assertTrue(login)
        # check for username
        self.assertEqual(self.user.username, 'teacher1')

class StudentRegisterViewTest(TestCase):

    def setUp(self):
        # create two students 
        test_user1 = User.objects.create_user(username='student1', password='3M<IKHSDFkds+tiM!')
        test_user2 = User.objects.create_user(username='student2', password='8MN1vDSFJN183?')

        test_user1.save()
        test_user2.save()

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

    def test__for_login_restriction_permission_and_template(self):
        response = self.client.get(reverse('coursemateapp:student'))
        self.assertRedirects(response, '/coursemateapp/login/?next=/coursemateapp/student/')
        self.user = User.objects.get(username="student1")
        login = self.client.login(username='student1', password='wrong')
        self.assertFalse(login)
        login = self.client.login(username='student1', password='3M<IKHSDFkds+tiM!')
        self.assertTrue(login)
        self.assertEqual(self.user.username, 'student1')

class LoginPageViewTest(TestCase):

    def setUp(self):
        # create two users 
        test_user1 = User.objects.create_user(username='student1', password='3M<IKHSDFkds+tiM!')
        test_user2 = User.objects.create_user(username='teacher1', password='8MN1vDSFJN183?')

        test_user1.save()
        test_user2.save()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/coursemateapp/login/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('coursemateapp:login'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('coursemateapp:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
    

class StudentViewTest(TestCase):

    def setUp(self):
        # create two students 
        test_user1 = User.objects.create_user(username='student1', password='3M<IKHSDFkds+tiM!')
        test_user2 = User.objects.create_user(username='student2', password='8MN1vDSFJN183?')

        test_user1.save()
        test_user2.save()

        group = Group(name="student")
        group.save()
        user = User.objects.get(username="student1") 
        user.groups.add(group) 

    def test__for_login_restriction_permission_and_template(self):
        response = self.client.get(reverse('coursemateapp:student'))
        self.assertRedirects(response, '/coursemateapp/login/?next=/coursemateapp/student/')
        self.user = User.objects.get(username="student1")
        login = self.client.login(username='student1', password='3M<IKHSDFkds+tiM!')
        self.assertTrue(login)
        self.assertEqual(self.user.username, 'student1')
        response = self.client.get(reverse('coursemateapp:student'))
        self.assertEqual(response.status_code, 200)
    
class StudentRestrictedViewsTest(TestCase):
    def setUp(self):
        # create two students 
        test_user1 = User.objects.create_user(username='student1', password='3M<IKHSDFkds+tiM!')
        test_user2 = User.objects.create_user(username='student2', password='8MN1vDSFJN183?')

        test_user1.save()
        test_user2.save()

        group = Group(name="student")
        group.save()
        user = User.objects.get(username="student1") 
        user.groups.add(group) 
    
    # upload assessment view 
    def test_view_url_exists_at_desired_location_upload(self):
        response = self.client.get('/coursemateapp/student/upload-assessment')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name_upload(self):
        response = self.client.get(reverse('coursemateapp:upload'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template_upload(self):
        response = self.client.get(reverse('coursemateapp:upload'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'upload.html')
    
    # write review view
    def test_view_url_exists_at_desired_location_review(self):
        response = self.client.get('/coursemateapp/student/write-review')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name_review(self):
        response = self.client.get(reverse('coursemateapp:writereview'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template_review(self):
        response = self.client.get(reverse('coursemateapp:writereview'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'writereview.html')
    
    #export grade view 
    def test_view_url_exists_at_desired_location_review(self):
        response = self.client.get('/coursemateapp/student/export-grade')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name_review(self):
        response = self.client.get(reverse('coursemateapp:export'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template_review(self):
        response = self.client.get(reverse('coursemateapp:export'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'export.html')

class TeacherViewTest(TestCase):
    def setUp(self):
        # create two students 
        test_user1 = User.objects.create_user(username='teacher1', password='3M<IKHSDFkds+tiM!')
        test_user1.save()

        group = Group(name="teacher")
        group.save()
        user = User.objects.get(username="teacher1") 
        user.groups.add(group) 
    
    def test__with_login_restriction_permission_and_template(self):
        response = self.client.get(reverse('coursemateapp:teacher'))
        self.assertRedirects(response, '/coursemateapp/login/?next=/coursemateapp/teacher/')
        self.user = User.objects.get(username="teacher1")
        login = self.client.login(username='teacher1', password='3M<IKHSDFkds+tiM!')
        self.assertTrue(login)
        self.assertEqual(self.user.username, 'teacher1')
        response = self.client.get(reverse('coursemateapp:teacher'))
        self.assertEqual(response.status_code, 200)

        # TEACHER VIEW TESTS 
        # url location
        response = self.client.get('/coursemateapp/teacher/')
        self.assertEqual(response.status_code, 200)
        # accessible by name 
        response = self.client.get(reverse('coursemateapp:teacher'))
        self.assertEqual(response.status_code, 200)
        # uses correct tempalte 
        response = self.client.get(reverse('coursemateapp:teacher'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teacher.html')


    


