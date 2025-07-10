import unittest
from tax_calculator import calculate_tax

class TestTaxCalculator(unittest.TestCase):
    # First test: earnings below 12000 should pay no tax
    def test_no_tax_below_12000(self):
        self.assertEqual(calculate_tax(10000), 0)

if __name__ == '__main__':
    unittest.main()
