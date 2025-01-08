
import unittest
from finance_formulas import Finance


class TestFinances(unittest.TestCase):
    def test_cash_flow(self):
        t1 = Finance()
        self.assertTrue(t1.cash_flow(10000, 5500), 4500)

    def test_net_worth(self):
        t1 = Finance()
        self.assertTrue(t1.net_worth(10000, 5500), 4500)

    def test_net_income(self):
        t1 = Finance()
        self.assertEqual(t1.net_income(10000, 5500), 4500)

    def test_simple_interest(self):
        t1 = Finance()
        self.assertEqual(t1.simple_interest(100, 0.3, 5), 150.0)

    def test_gains_or_losses(self):
        ti = Finance()
        self.assertEqual(ti.gain_or_lose(3, 2), 0.5)


if __name__ == '__main__':
    # unittest.TestCase()
    unittest.main(argv=['ignored', '-v'], exit=False)