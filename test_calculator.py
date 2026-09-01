# test_calculator.py
import unittest

from operator import add, sub as subtract, mul as multiply

from calculator import (
    divide, power, square_root, percentage,
)


class TestArithmetic(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(1, 0)


class TestPower(unittest.TestCase):
    def test_power(self):
        self.assertEqual(power(2, 3), 8)

    def test_power_zero_negative(self):
        with self.assertRaises(ValueError):
            power(0, -1)

    def test_power_exponent_too_large(self):
        with self.assertRaises(ValueError):
            power(2, 500)

    def test_power_result_too_large(self):
        with self.assertRaises(ValueError):
            power(1e200, 2)


class TestSquareRoot(unittest.TestCase):
    def test_square_root(self):
        self.assertEqual(square_root(9), 3)

    def test_square_root_negative(self):
        with self.assertRaises(ValueError):
            square_root(-4)


class TestPercentage(unittest.TestCase):
    def test_percentage(self):
        self.assertEqual(percentage(200, 10), 20)

    def test_percentage_zero(self):
        self.assertEqual(percentage(100, 0), 0)

    def test_percentage_negative(self):
        with self.assertRaises(ValueError):
            percentage(100, -50)


if __name__ == "__main__":
    unittest.main()
