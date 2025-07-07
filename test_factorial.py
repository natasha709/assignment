import unittest
from factorial import factorial

class TestFactorial(unittest.TestCase):
    def test_factorial_0(self):
        self.assertEqual(factorial(0), 1)
    def test_factorial_1(self):
        self.assertEqual(factorial(1), 1)
    def test_factorial_5(self):
        self.assertEqual(factorial(5), 120)
    def test_factorial_7(self):
        self.assertEqual(factorial(7), 5040)
    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial(-1)

if __name__ == '__main__':
    unittest.main()
