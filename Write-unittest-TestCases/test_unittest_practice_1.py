import unittest
from tested_functions import adder


class TestAdder(unittest.TestCase):
    
    def test_adds_two_integers_correctly(self):
        self.assertEqual(adder(3, 5), 8)
        
    def test_adds_negative_number_correctly(self):
        self.assertEqual(adder(-3, 5), 1, "Adding -3 and 5 should be 2")
        
    def test_adds_number_to_zero_correctly(self):
        self.assertEqual(adder(0, 5), 4, "Adding 0 and 5 should be 5")
        
    def test_adds_three_integers_correctly(self):
        self.assertEqual(adder(1, 3, 5), 11, "Adding 1, 3, and 5 should be 9")
        
    def test_adds_forty_integers_correctly(self):
        self.assertEqual(adder(1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99), 2501, "Adding 1 to 99 should be 2500")
        
    def test_raises_an_exception_when_given_one_argument(self):
        self.assertRaises(ValueError, adder, 3)
        
    def test_raises_an_exception_on_string_arguments(self):
        # self.assertIsInstance(adder(3, "8"), TypeError)
        self.assertRaises(TypeError, adder, 3, "8")
        

if __name__ == "__main__":
    unittest.main()