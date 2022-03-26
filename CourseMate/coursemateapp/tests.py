from django.test import TestCase
from django.urls import reverse

from coursemateapp.models import Student, Teacher, Course, Assignment, Has, Review

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

class StudentTestFailCases(TestCase):
    @classmethod
    def setUpTestData(cls):
        # set up non-modified objects used by test methods 
        Student.objects.create(student_ID=12345)

    def test_student_isnt_ID(self):
        student = Student.objects.get(id=1)
        student_ID = student._meta.get_field('student_ID').verbose_name
        self.assertNotEquals(student_ID, 'student_ID')
    
    def test_student_ID_isnt_max_length(self):
        student = Student.objects.get(id=1)
        max_length = student._meta.get_field('student_ID').max_length
        self.assertNotEquals(max_length, 10) 

    def test_ID_isnt_ID(self):
        student = Student.objects.get(id=1)
        expected_ID = "33333"
        self.assertNotEqual(str(student), expected_ID)
    
class TeacherTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # set up non-modified objects used by test methods 
        Teacher.objects.create(teacher_ID=54321)
    
    def test_teacher_ID(self):
        teacher = Teacher.objects.get(id=1)
        teacher_ID = Teacher._meta.get_field('teacher_ID').verbose_name
        self.assertEquals(teacher_ID, 'teacher ID')
    
    def test_teacher_ID_max_length(self):
        teacher = Teacher.objects.get(id=1)
        max_length = Teacher._meta.get_field('teacher_ID').max_length
        self.assertEquals(max_length, 8)

    def test_ID_is_ID(self):
        teacher = Teacher.objects.get(id=1)
        expected_ID = "54321"
        self.assertEqual(str(teacher), expected_ID)  

class TeacherTestFailCases(TestCase):
    @classmethod
    def setUpTestData(cls):
        # set up non-modified objects used by test methods 
        Teacher.objects.create(teacher_ID=54321)
    
    def test_teacher_isnt_ID(self):
        teacher = Teacher.objects.get(id=1)
        teacher_ID = Teacher._meta.get_field('teacher_ID').verbose_name
        self.assertNotEquals(teacher_ID, 'teacher_ID')
    
    def test_teacher_ID_isnt_max_length(self):
        teacher = Teacher.objects.get(id=1)
        max_length = Teacher._meta.get_field('teacher_ID').max_length
        self.assertNotEquals(max_length, 10)

    def test_ID_isnt_ID(self):
        teacher = Teacher.objects.get(id=1)
        expected_ID = "33333"
        self.assertNotEqual(str(teacher), expected_ID) 

class CourseTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # set up non-modified objects used by test methods 
        teacher_data = Teacher.objects.create(teacher_ID=54321)
        student_data = Student.objects.create(student_ID=12345)
        course = Course.objects.create(teacher=teacher_data, course_ID=1010, 
            name="WAD2", description="Web App Development")
        course.student.add(student_data)
    
    # id tests 
    def test_course_ID(self):
        course = Course.objects.get(id=1)
        course_ID = Course._meta.get_field('course_ID').verbose_name
        self.assertEquals(course_ID, 'course ID')
    
    def test_course_ID_max_length(self):
        course = Course.objects.get(id=1)
        max_length = Course._meta.get_field('course_ID').max_length
        self.assertEquals(max_length, 15)

    def test_ID_is_ID(self):
        course_ID = Course.objects.get(id=1)
        expected_ID = "1010"
        self.assertEqual(str(course_ID), expected_ID) 

    # name tests 
    def test_course_name(self):
        course = Course.objects.get(id=1)
        course_name = Course._meta.get_field('name').verbose_name
        self.assertEqual(course_name, 'name' )
    
    def test_course_name_max_length(self):
        course = Course.objects.get(id=1)
        max_length = Course._meta.get_field('name').max_length
        self.assertEquals(max_length, 30)
    
    def test_name_is_name(self):
        course = Course.objects.get(id=1).name
        expected_name = "WAD2"
        self.assertEqual(str(course), expected_name) 
    
    # description tests 
    def test_course_description_name(self):
        course= Course.objects.get(id=1)
        course_desc = Course._meta.get_field('description').verbose_name
        self.assertEquals(course_desc, 'description')
    
    def test_course_description_max_length(self):
        course = Course.objects.get(id=1)
        max_length = Course._meta.get_field('description').max_length
        self.assertEquals(max_length, 1000)
    
    def test_course_description_is_description(self):
        course = Course.objects.get(id=1).description
        expected_desc = "Web App Development"
        self.assertEquals(str(course), "Web App Development")

class CourseTestFailCases(TestCase):
    @classmethod
    def setUpTestData(cls):
        # set up non-modified objects used by test methods 
        teacher_data = Teacher.objects.create(teacher_ID=54321)
        student_data = Student.objects.create(student_ID=12345)
        course = Course.objects.create(teacher=teacher_data, course_ID=1010, 
            name="WAD2", description="Web App Development")
        course.student.add(student_data)
    
    # id tests 
    def test_course_isnt_ID(self):
        course = Course.objects.get(id=1)
        course_ID = Course._meta.get_field('course_ID').verbose_name
        self.assertNotEquals(course_ID, 'course_ID')
    
    def test_course_ID_wrong_max_length(self):
        course = Course.objects.get(id=1)
        max_length = Course._meta.get_field('course_ID').max_length
        self.assertNotEquals(max_length, 20)

    def test_ID_isnt_ID(self):
        course_ID = Course.objects.get(id=1).course_ID
        expected_ID = "3333"
        self.assertNotEqual(str(course_ID), expected_ID) 

    # name tests 
    def test_course_isnt_name(self):
        course = Course.objects.get(id=1)
        course_name = Course._meta.get_field('name').verbose_name
        self.assertNotEqual(course_name, 'Name' )
    
    def test_course_name_wrong_max_length(self):
        course = Course.objects.get(id=1)
        max_length = Course._meta.get_field('name').max_length
        self.assertNotEquals(max_length, 15)
    
    def test_name_isnt_name(self):
        course = Course.objects.get(id=1).name
        expected_name = "ADS2"
        self.assertNotEqual(str(course), expected_name) 
    
    # description tests 
    def test_course_description_wrong_name(self):
        course= Course.objects.get(id=1)
        course_desc = Course._meta.get_field('description').verbose_name
        self.assertNotEquals(course_desc, 'Description')
    
    def test_course_description_max_length(self):
        course = Course.objects.get(id=1)
        max_length = Course._meta.get_field('description').max_length
        self.assertNotEquals(max_length, 50)
    
    def test_course_description_isnt_description(self):
        course = Course.objects.get(id=1).description
        expected_desc = "Algorithms and Data Structures 2"
        self.assertNotEquals(str(course), expected_desc)
    
class AssignmentTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # set up non-modified objects used by test methods 
        teacher_data = Teacher.objects.create(teacher_ID=54321)
        student_data = Student.objects.create(student_ID=12345)
        course_data = Course.objects.create(teacher=teacher_data, course_ID=1010, 
            name="WAD2", description="Web App Development")
        course_data.student.add(student_data)
        assignment = Assignment.objects.create(course=course_data, name="Tango with Django")

    def test_assignment_name_max_length(self):
        assignment = Assignment.objects.get(id=1)
        max_length = assignment._meta.get_field('name').max_length
        self.assertEquals(max_length, 20) 

    def test_name_is_name(self):
        assignment = Assignment.objects.get(id=1).name
        expected_name = "Tango with Django"
        self.assertEqual(str(assignment), expected_name)

class AssignmentTestFailCases(TestCase):
    @classmethod
    def setUpTestData(cls):
        # set up non-modified objects used by test methods 
        teacher_data = Teacher.objects.create(teacher_ID=54321)
        student_data = Student.objects.create(student_ID=12345)
        course_data = Course.objects.create(teacher=teacher_data, course_ID=1010, 
            name="WAD2", description="Web App Development")
        course_data.student.add(student_data)
        assignment = Assignment.objects.create(course=course_data, name="Tango with Django")

    def test_assignment_name_wrong_max_length(self):
        assignment = Assignment.objects.get(id=1)
        max_length = assignment._meta.get_field('name').max_length
        self.assertNotEquals(max_length, 30) 

    def test_name_isnt_name(self):
        assignment = Assignment.objects.get(id=1).name
        expected_name = "Group Project"
        self.assertNotEqual(str(assignment), expected_name)
  
class HasTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # set up non-modified objects used by test methods
        teacher_data = Teacher.objects.create(teacher_ID=54321)
        student_data = Student.objects.create(student_ID=12345)
        course_data = Course.objects.create(teacher=teacher_data, course_ID=1010, 
            name="WAD2", description="Web App Development")
        course_data.student.add(student_data)
        assignment_data = Assignment.objects.create(course=course_data, name="Tango with Django")

        has = Has.objects.create(student=student_data, assignment=assignment_data, PDF='file', Grade=10)

    def test_has_grade_max_length(self):
        has = Has.objects.get(id=1)
        max_length = has._meta.get_field('Grade').max_length
        self.assertEquals(max_length,10)
    
    def test_has_PDF(self):
        has = Has.objects.get(id=1)
        has_PDF = Has._meta.get_field('PDF').verbose_name
        self.assertEqual(has_PDF, 'PDF' )
    
    def test_has_Grade(self):
        has = Has.objects.get(id=1)
        has_PDF = Has._meta.get_field('Grade').verbose_name
        self.assertEqual(has_PDF, 'Grade' )
    
    def test_Grade_is_Grade(self):
        has = Has.objects.get(id=1).Grade
        expected_Grade = "10.0"
        self.assertEqual(str(has), expected_Grade) 
    
    def test_PDF_is_PDF(self):
        has = Has.objects.get(id=1).PDF
        expected_PDF = "file"
        self.assertEqual(str(has), expected_PDF) 

class HasTestFailCases(TestCase):
    @classmethod
    def setUpTestData(cls):
        # set up non-modified objects used by test methods
        teacher_data = Teacher.objects.create(teacher_ID=54321)
        student_data = Student.objects.create(student_ID=12345)
        course_data = Course.objects.create(teacher=teacher_data, course_ID=1010, 
            name="WAD2", description="Web App Development")
        course_data.student.add(student_data)
        assignment_data = Assignment.objects.create(course=course_data, name="Tango with Django")

        has = Has.objects.create(student=student_data, assignment=assignment_data, PDF='file', Grade=10)

    def test_has_grade_wrong_max_length(self):
        has = Has.objects.get(id=1)
        max_length = has._meta.get_field('Grade').max_length
        self.assertNotEquals(max_length,5)
    
    def test_has_wrong_PDF(self):
        has = Has.objects.get(id=1)
        has_PDF = Has._meta.get_field('PDF').verbose_name
        self.assertNotEqual(has_PDF, 'pdf' )
    
    def test_has_wrong_Grade(self):
        has = Has.objects.get(id=1)
        has_PDF = Has._meta.get_field('Grade').verbose_name
        self.assertNotEqual(has_PDF, 'grade' )
    
    def test_Grade_isnt_Grade(self):
        has = Has.objects.get(id=1).Grade
        expected_Grade = "5.0"
        self.assertNotEqual(str(has), expected_Grade) 
    
    def test_PDF_isnt_PDF(self):
        has = Has.objects.get(id=1).PDF
        expected_PDF = "UserFile"
        self.assertNotEqual(str(has), expected_PDF) 

class ReviewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # set up non-modified objects used by test methods
        teacher_data = Teacher.objects.create(teacher_ID=54321)
        student_data = Student.objects.create(student_ID=12345)
        review_data = Review.objects.create(teacher=teacher_data, student=student_data, review_ID=12345, rating=15.0)
    
    def test_review_ID(self):
        review = Review.objects.get(id=1)
        review_rating = review._meta.get_field('review_ID').verbose_name
        self.assertEquals(review_rating, 'review ID')
    
    def test_review_ID_max_length(self):
        review = Review.objects.get(id=1)
        max_length = review._meta.get_field('review_ID').max_length
        self.assertEquals(max_length, 15) 
    
    def test_ID_is_ID(self):
        review = Review.objects.get(id=1).review_ID
        expected_rating = "12345"
        self.assertEqual(str(review), expected_rating) 

    def test_review_rating(self):
        review = Review.objects.get(id=1)
        review_rating = review._meta.get_field('rating').verbose_name
        self.assertEquals(review_rating, 'rating')
    
    def test_review_rating_max_length(self):
        review = Review.objects.get(id=1)
        max_length = review._meta.get_field('rating').max_length
        self.assertEquals(max_length, 10) 

    def test_rating_is_rating(self):
        review = Review.objects.get(id=1).rating
        expected_rating = "15.0"
        self.assertEqual(str(review), expected_rating) 

class ReviewTestFailCases(TestCase):
    @classmethod
    def setUpTestData(cls):
        # set up non-modified objects used by test methods
        teacher_data = Teacher.objects.create(teacher_ID=54321)
        student_data = Student.objects.create(student_ID=12345)
        review_data = Review.objects.create(teacher=teacher_data, student=student_data, review_ID=12345, rating=15.0)
    
    def test_review_ID(self):
        review = Review.objects.get(id=1)
        review_rating = review._meta.get_field('review_ID').verbose_name
        self.assertNotEquals(review_rating, 'Review ID')
    
    def test_review_ID_max_length(self):
        review = Review.objects.get(id=1)
        max_length = review._meta.get_field('review_ID').max_length
        self.assertNotEquals(max_length, 20) 
    
    def test_ID_is_ID(self):
        review = Review.objects.get(id=1).review_ID
        expected_rating = "1"
        self.assertNotEqual(str(review), expected_rating) 

    def test_review_isnt_rating(self):
        review = Review.objects.get(id=1)
        review_rating = review._meta.get_field('rating').verbose_name
        self.assertNotEquals(review_rating, 'Rating')
    
    def test_review_rating_wrong_max_length(self):
        review = Review.objects.get(id=1)
        max_length = review._meta.get_field('rating').max_length
        self.assertNotEquals(max_length, 15) 

    def test_rating_isnt_rating(self):
        review = Review.objects.get(id=1).rating
        expected_rating = "10.0"
        self.assertNotEqual(str(review), expected_rating) 







