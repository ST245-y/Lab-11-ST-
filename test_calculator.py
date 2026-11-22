# https://github.com/ST245-y/Lab-11-ST-/tree/main
# Partner 1: Sakshi Tripathy
# Partner 2: Completed independently (no partner)

import unittest
import math
import calculator


class TestCalculator(unittest.TestCase):

    # Partner 1 tests

    def test_add(self):
        self.assertEqual(calculator.add(5, 3), 8)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(5, 3), 15)

    def test_divide(self):
        self.assertEqual(calculator.divide(2, 10), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(0, 10)

    def test_logarithm(self):
        self.assertAlmostEqual(calculator.logarithm(2, 8), 3)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(2, 0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 8)

    # Partner 2 tests

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5)

    def test_sqrt(self):
        self.assertAlmostEqual(calculator.square_root(25), 5)

        with self.assertRaises(ValueError):
            calculator.square_root(-4)

    # Additional tests

    def test_exponent(self):
        self.assertEqual(calculator.exponent(2, 3), 8)

    def test_negative_hypotenuse_inputs(self):
        self.assertAlmostEqual(calculator.hypotenuse(-3, -4), 5)


if __name__ == "__main__":
    unittest.main()
