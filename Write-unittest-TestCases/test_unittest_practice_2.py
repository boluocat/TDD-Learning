import unittest
from tested_functions import divider


class TestDivider(unittest.TestCase):
    """Requirements to test:
    
        - Returns non-integer results (does not floor divide)
        - Raises ValueError if too many or too few arguments provided (division is binary)
        - Raises TypeError if non-integer arguments provided
        - Raises ValueError if attempting to divide by 0 (treating the error as a bad argument issue, not a math issue)
        - Handles arbitrarily large integer dividends/divisors
        - Can be called multiple times in succession accurately (divider(divider(divider(...
    """
    
    def test_divides_two_integer_correctly(self):
        self.assertEqual(divider(10, 2), 5)
        
    def test_returns_non_integer_results(self):
        self.assertEqual(divider(7, 2), 3.5)
    
    def test_raises_exception_on_too_few_arguments(self):
        self.assertRaises(ValueError, divider, 3)
        
    def test_raises_exception_on_too_many_arguments(self):
        self.assertRaises(ValueError,  divider, 3, 5, 7)
        
    def test_raises_exception_on_non_integer_arguments(self):
        self.assertRaises(TypeError, divider, 3, "8")
        
    def test_raises_exception_on_dividing_by_zero(self):
        self.assertRaises(ValueError, divider, 3, 0)
        
    def test_handles_large_integers(self):
        large_dividend = 10**100
        large_divisor = 10**50
        self.assertEqual(divider(large_dividend, large_divisor), 10**50)
        
    def test_multiple_successive_calls(self):
        self.assertEqual(divider(divider(divider(1000, 10), 10), 10), 1)
        
        
if __name__ == "__main__":
    unittest.main()