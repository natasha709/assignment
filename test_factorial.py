import unittest
from factorial import factorial

class TestFactorial(unittest.TestCase):
    # Test for factorial of 0 (edge case, should return 1)
    def test_factorial_0(self):
        self.assertEqual(factorial(0), 1)
    # Test for factorial of 1 (should return 1)
    def test_factorial_1(self):
        self.assertEqual(factorial(1), 1)
    # Test for factorial of 5 (should return 120)
    def test_factorial_5(self):
        self.assertEqual(factorial(5), 120)
    # Test for factorial of 7 (should return 5040)
    def test_factorial_7(self):
        self.assertEqual(factorial(7), 5040)
    # Test for negative input (should raise ValueError)
    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial(-1)

if __name__ == '__main__':
    unittest.main()
