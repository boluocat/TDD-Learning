import unittest
import compute_stats_refactor

class TestnewFunction(unittest.TestCase):
    def test_harmonic_mean(self):
        self.assertEqual(compute_stats_refactor.harmonic_mean([2, 3, 4, 5]), 3.116883116883117)
        
    def test_variance(self):
        self.assertEqual(compute_stats_refactor.variance([2, 3, 4, 5]), 1.25) 
        
    def test_standard_deviation(self):
        self.assertEqual(compute_stats_refactor.standard_dev([2, 3, 4, 5]), 1.118033988749895)
        
        
if __name__ == '__main__':
    unittest.main(argv=['ignore', '-v'], exit=False)