from django.test import TestCase

from coursemateapp.models import Student, Teacher

# Create your tests here.
    
class StudentTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # set up non-modified objects used by test methods 
        Student.objects.create(student_ID=12345)

    def test_student_ID(self):
        student = Student.objects.get(id=1)
        student_ID = student._meta.get_field('student_ID').verbose_name
        self.assertEquals(student_ID, 'student ID')
    
    def test_student_ID_max_length(self):
        student = Student.objects.get(id=1)
        max_length = student._meta.get_field('student_ID').max_length
        self.assertEquals(max_length, 8) 

    def test_ID_is_ID(self):
        student = Student.objects.get(id=1)
        expected_ID = "12345"
        self.assertEqual(str(student), expected_ID)
    
class TeacherTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # set up non-modified objects used by test methods 
        Teacher.objects.create(teacher_ID=54321)
    
    def test_teacher_ID(self):
        teaher = Teacher.objects.get(id=1)
        teacher_ID = Teacher._meta.get_field('teacher_ID').verbose_name
        self.assertEquals(teacher_ID, 'teacher ID')
    
    def test_teacher_ID_max_length(self):
        teaher = Teacher.objects.get(id=1)
        max_length = Teacher._meta.get_field('teacher_ID').max_length
        self.assertEquals(max_length, 8)

    def test_ID_is_ID(self):
        teacher = Teacher.objects.get(id=1)
        expected_ID = "54321"
        self.assertEqual(str(teacher), expected_ID)       


