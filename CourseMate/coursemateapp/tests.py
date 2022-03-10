from django.test import TestCase

# Create your tests here.

class TestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass 
    
    def setUp(self):
        print("setUp: RUn once for every test method to setup clean data.")
        pass 
    
    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)
    
    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(False)
    
    def test_one_plus_one_equals_two(self):
        print("Method: test)one_plus_one_equals_two.")
        self.assertEquals(1 + 1, 2)
    
    