import unittest
from tax_calculator import calculate_tax

class TestTaxCalculator(unittest.TestCase):
    # First test: earnings below 12000 should pay no tax
    def test_no_tax_below_12000(self):
        self.assertEqual(calculate_tax(10000), 0)
    # Second test: earnings exactly 12000 should pay no tax
    def test_no_tax_at_12000(self):
        self.assertEqual(calculate_tax(12000), 0)
    # Third test: earnings just above 12000 should pay 20% on the amount above 12000
    def test_tax_just_above_12000(self):
        self.assertEqual(calculate_tax(13000), 200)
    # Fourth test: earnings at 36000 should pay 20% on 24000
    def test_tax_at_36000(self):
        self.assertEqual(calculate_tax(36000), 4800)
    # Fifth test: earnings above 36000 should pay 20% on 24000 and 40% on the rest
    def test_tax_above_36000(self):
        self.assertEqual(calculate_tax(40000), 4800 + 1600)

if __name__ == '__main__':
    unittest.main()
