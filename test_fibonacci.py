import unittest
from fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):
    # Test for the first TDD cycle: fibonacci(0) == 0
    def test_fibonacci_0(self):
        self.assertEqual(fibonacci(0), 0)
    # Test for the second TDD cycle: fibonacci(1) == 1
    def test_fibonacci_1(self):
        self.assertEqual(fibonacci(1), 1)
    # Test for the third TDD cycle: fibonacci(2) == 1
    def test_fibonacci_2(self):
        self.assertEqual(fibonacci(2), 1)
    # Test for the fourth TDD cycle: fibonacci(5) == 5
    def test_fibonacci_5(self):
        self.assertEqual(fibonacci(5), 5)
    # Test for the fifth TDD cycle: fibonacci(10) == 55
    def test_fibonacci_10(self):
        self.assertEqual(fibonacci(10), 55)
    # Test for negative input
    def test_fibonacci_negative(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)

if __name__ == '__main__':
    unittest.main()
