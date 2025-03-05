"""
Contains all of the unit tests for
random_person_generator.py.
Since the random module was used heavily
in random_person_generator.py, mock objects
were used to facilitate testing.
"""

import unittest
import random_person_generator as r
from unittest.mock import patch


class TestRandomPerson(unittest.TestCase):

    @patch('random_person_generator.male_first_name')
    def test_read_male_first_names(self, mocked):
        mocked.return_value = 'Matt'
        self.assertEqual(r.male_first_name(), 'Matt')

    @patch('random_person_generator.female_first_name')
    def test_read_female_names(self, mocked):
        mocked.return_value = 'Sally'
        self.assertEqual(r.female_first_name(), 'Sally')

    @patch('random_person_generator.surname')
    def test_read_surnames(self, mocked):
        mocked.return_value = 'Johnson'
        self.assertEqual(r.surname(), 'Johnson')

    @patch('random_person_generator.generate_random_name')
    def test_read_random_name(self, mocked):
        mocked.return_value = 'Kevin Overall'
        self.assertEqual(r.generate_random_name(), 'Kevin Overall')

    @patch('random_person_generator.random_age')
    def test_random_name(self, mocked):
        mocked.return_value = 25
        self.assertEqual(r.random_age(), 25)

    @patch('random_person_generator.random_email_service')
    def test_random_email_service(self, mocked):
        mocked.return_value = 'gmail'
        self.assertEqual(r.random_email_service(), 'gmail')

    @patch('random_person_generator.random_phone_number')
    def test_random_phone_number(self, mocked):
        mocked.return_value = '723-723-8623'
        self.assertEqual(r.random_phone_number(), '723-723-8623')

    @patch('random_person_generator.create_occupation')
    def test_occupation(self, mocked):
        mocked.return_value = 'programmer'
        self.assertEqual(r.create_occupation(), 'programmer')

    @patch('random_person_generator.create_person')
    def test_create_person(self, mocked):
        mocked.return_value = """{'first_name': 'Darnell', 'last_name': 'Tannenbaum', 'email': " \
                              "'darnell.tannenbaum@aol.com', 'sex': 'female', 'age': 20, " \
                              "'job': 'programmer', 'phone': '232-40-882'}'
                            """
        self.assertEqual(r.create_person(), """{'first_name': 'Darnell', 'last_name': 'Tannenbaum', 'email': " \
                              "'darnell.tannenbaum@aol.com', 'sex': 'female', 'age': 20, " \
                              "'job': 'programmer', 'phone': '232-40-882'}'
                            """)


if __name__ == '__main__':
    unittest.main()