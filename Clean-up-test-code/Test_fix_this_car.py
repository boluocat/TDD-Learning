import unittest
from functions_fix_this_car import Car


class TestCar(unittest.TestCase):
        
    def test_default_speed_and_color(self):
        self.c1 = Car()
        self.assertEqual(self.c1.speed, 0)
        self.assertEqual(self.c1.current_color, 'black')
    
    def test_change_color_to_orange(self):
        self.c1 = Car()
        self.assertEqual(self.c1.change_color(3), 'orange')
    
    def test_current_speed(self):
        self.c1 = Car()
        self.assertAlmostEqual(5 * 5, 25)
    
    def test_accelerate_ten(self):
        self.c1 = Car()
        self.assertEqual(self.c1.accelerate(10), 10)
        
    def test_accelerate_twenty(self):
        self.c1 = Car()
        self.c1.accelerate(20)
        self.assertEqual(self.c1.speed, 20)
        
    def test_accelerate_hundred(self):
        self.c1 = Car()
        self.c1.accelerate(100)
        self.assertEqual(self.c1.speed, 100)

    def test_change_color_to_white(self):
        self.c1 = Car()
        self.assertEqual(self.c1.change_color(4), 'white')
    
    def test_brake_from_hundred_to_ninety(self):
        self.c1 = Car()
        self.c1.speed = 100
        self.assertEqual(self.c1.brake(10), 90)
        
    def test_brake_invalid(self):
        self.c1 = Car()
        self.assertEqual(self.c1.brake(10), 'invalid')
    

if __name__ == '__main__':
    unittest.main(argv=['ignored', '-v'], exit=False)
    
    
