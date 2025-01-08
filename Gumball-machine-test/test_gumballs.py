import unittest

class TestGumBalls(unittest.TestCase):
    
    # maximum number of gumballs in the machine
    def test_max_gumballs(self):
        self.assertEqual(1000, 1000)
        
    # cost of each transaction
    def test_cost_per_transaction(self):
        self.assertEqual(0.75, 0.75)
        
    # number of gumballs of each transaction
    def test_number_of_gumballs_per_transaction(self):
        self.assertEqual(3, 3)
        
    # minimum number of gumballs in the machine
    def test_min_gumballs(self):
        self.assertEqual(100, 100)

if __name__ == '__main__':
    unittest.main(argv=['ignored', '-v'], exit=False)