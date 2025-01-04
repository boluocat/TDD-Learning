import unittest

class Functions():
    def adder(self, x, y):
        return x + y
    
# You can define multiple test classes in the same file, and named them without starting with "test", it can still be identified as a test class
class uux(unittest.TestCase):
    
    # But, if you test case function is not starting with "test", it won't be identified a test case. So, This test will not run.
    def adds_three_and_five_correctly_test(self):
        self.assertEqual(Functions().adder(3,5), 8, "Adding 3 and 5 should produce 8")
        print("this is uux")

class TestAdder(unittest.TestCase):
        
    def testadds_two_and_one_correctly(self):
        self.assertEqual(Functions().adder(2,1), 3, "Adding 2 and 1 should produce 3")
        print("Test passed")
        
    def test_adds_floating_point_numbers_correctly(self):
        result1 = Functions().adder(1, 1/3)
        result2 = Functions().adder(result1, -1)
        result3 = result2*3
        self.assertEqual(result3, 1, "Should still provide integer output despite floating point input")
        
    # def test_adds_integer_and_string_raises_exception(self):
    #     # try:
    #     #     result = adder(3, "12")
    #     # except Exception as e:
    #     #     self.assertIsInstance(e, TypeError)
    #     # else:
    #     #     self.fail("Did not raise Exception")
            
    #     self.assertRaises(TypeError, Functions().adder, 3, 12)
        
        
if __name__ == '__main__':
    unittest.main()