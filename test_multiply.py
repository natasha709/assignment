import unittest
from multiply import multiply

class TestMultiply(unittest.TestCase):
    def test_multiply_1_1(self):
        self.assertEqual(multiply(1, 1), 1)
    def test_multiply_2_2(self):
        self.assertEqual(multiply(2, 2), 4)
    def test_multiply_3_3(self):
        self.assertEqual(multiply(3, 3), 9)
    def test_multiply_4_4(self):
        self.assertEqual(multiply(4, 4), 16)
    def test_multiply_23_45(self):
        self.assertEqual(multiply(23, 45), 23 * 45)

if __name__ == '__main__':
    unittest.main()
