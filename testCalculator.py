import unittest
from calculator import Calculator

class CalculatorTests(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        result = self.calculator.add(2, 3)
        self.assertEqual(result, 5)

    def test_subtraction(self):
        result = self.calculator.subtract(5, 3)
        self.assertEqual(result, 2)

    def test_multiplication(self):
        result = self.calculator.multiply(2, 3)
        self.assertEqual(result, 6)

    def test_division(self):
        result = self.calculator.divide(6, 3)
        self.assertEqual(result, 2)

    def test_addition_negative_numbers(self):
        result = self.calculator.add(-5, -3)
        self.assertEqual(result, -8)

    def test_subtraction_negative_numbers(self):
        result = self.calculator.subtract(-5, -3)
        self.assertEqual(result, -2)

    def test_multiplication_negative_numbers(self):
        result = self.calculator.multiply(-2, 3)
        self.assertEqual(result, -6)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.divide(6, 0)

if __name__ == '__main__':
    unittest.main()