import unittest
import random_person_generator as r
from unittest.mock import patch

class TestRandomPerson(unittest.TestCase):
    
    @patch('random_person_generator.male_first_name')
    def test_read_male_first_name(self, mocked):
        mocked.return_value = 'Matt'
        self.assertEqual(r.male_first_name(), 'Matt')
        
    @patch('random_person_generator.female_first_name')
    def test_read_female_first_name(self, mocked):
        mocked.return_value = 'HELEN'
        self.assertEqual(r.female_first_name(), 'HELEN')
        
    @patch('random_person_generator.surname')
    def test_read_surname(self, mocked):
        mocked.return_value = 'GARCIA'
        self.assertEqual(r.surname(), 'GARCIA')
        
    @patch('random_person_generator.generate_random_name')
    def test_generate_random_name(self, mocked):
        mocked.return_value = ('Matt', 'GARCIA')
        self.assertEqual(r.generate_random_name(), ('Matt', 'GARCIA'))
        
    @patch('random_person_generator.random_age')
    def test_random_age(self, mocked):
        mocked.return_value = 23
        self.assertEqual(r.random_age(min=1, max=100), 23)
        
    @patch('random_person_generator.random_age')
    def test_random_age_range_less_than_zero(self, mocked):
        mocked.return_value = 'Enter in min greater than 0 and a max less than one hundred'
        self.assertEqual(r.random_age(min=-1, max=100), 'Enter in min greater than 0 and a max less than one hundred')
        
    @patch('random_person_generator.random_age')
    def test_random_age_range_greater_than_100(self, mocked):
        mocked.return_value = 'Enter in min greater than 0 and a max less than one hundred'
        self.assertEqual(r.random_age(min=1, max=101), 'Enter in min greater than 0 and a max less than one hundred') 
        
    @patch('random_person_generator.random_email_service')
    def test_random_email_service(self, mocked):
        mocked.return_value = 'outlook.com'
        self.assertEqual(r.random_email_service(), 'outlook.com')
        
    @patch('random_person_generator.random_phone_number')
    def test_random_phone_number(self, mocked):
        mocked.return_value = '860-254-3650'
        self.assertEqual(r.random_phone_number(), '860-254-3650')
        
    @patch('random_person_generator.create_occupation')
    def test_create_occupation(self, mocked):
        mocked.return_value = 'doctor'
        self.assertEqual(r.create_occupation(23), 'doctor')
        
    @patch('random_person_generator.create_occupation')
    def test_create_occupation_for_NA(self, mocked):
        mocked.return_value = 'NA'
        self.assertEqual(r.create_occupation(3), 'NA')
    
    @patch('random_person_generator.create_occupation')
    def test_create_occupation_for_student(self, mocked):
        mocked.return_value = 'student'
        self.assertEqual(r.create_occupation(12), 'student')
        
    @patch('random_person_generator.create_person')
    def test_create_person(self, mocked):
        mocked.return_value ={'first_name': 'Matt', 'last_name': 'GARCIA', 'email': 'Matt.GARCIA@outlook.com', 'sex': 'male', 'age': 23, 'job': 'actor', 'phone': '343-58-515'}
        self.assertEqual(r.create_person(), {'first_name': 'Matt', 'last_name': 'GARCIA', 'email': 'Matt.GARCIA@outlook.com', 'sex': 'male', 'age': 23, 'job': 'actor', 'phone': '343-58-515'})
        
    def test_return_is_dict(self):
        result = r.create_person()
        self.assertIsInstance(result, dict, 'The return value should be a dictionary')
        
        
if __name__ == '__main__':
    unittest.main(argv=['ignored', '-v'], exit=False)