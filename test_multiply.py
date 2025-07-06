import unittest
from multiply import multiply

class TestMultiply(unittest.TestCase):
    def test_multiply_1_1(self):
        self.assertEqual(multiply(1, 1), 1)
    def test_multiply_2_2(self):
        self.assertEqual(multiply(2, 2), 4)

if __name__ == '__main__':
    unittest.main()
