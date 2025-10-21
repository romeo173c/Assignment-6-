import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
    def testAdd(self):
        self.assertEqual(self.calculator.calAdd(1, 8), 9)
    def testSubtract(self):
        self.assertEqual(self.calculator.calSubtract(7, 3), 4)
    def testMultiply(self):
        self.assertEqual(self.calculator.calMutiply(8, 4), 32)
    def testDivide(self):
        self.assertEqual(self.calculator.calDivide(15, 3), 5)


if __name__ == "__main__":
    unittest.main()