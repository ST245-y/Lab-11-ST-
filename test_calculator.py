
# https://github.com/ST245-y/Lab-11-ST-/tree/main
# Partner 1: Sakshi Tripathy
# Partner 2: Completed independently (no partner)

import unittest
import calculator


class TestCalculator(unittest.TestCase):

    # Partner 1 tests

    def test_add(self):
        self.assertEqual(calculator.add(5, 3), 8)
        self.assertEqual(calculator.add(-5, 3), -2)
        self.assertEqual(calculator.add(0, 0), 0)
        self.assertAlmostEqual(calculator.add(2.5, 1.5), 4.0)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(5, 3), 2)
        self.assertEqual(calculator.subtract(3, 5), -2)
        self.assertEqual(calculator.subtract(0, 0), 0)
        self.assertAlmostEqual(calculator.subtract(5.5, 2.5), 3.0)
        self.assertEqual(calculator.sub(8, 3), 5)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(5, 3), 15)
        self.assertEqual(calculator.multiply(-5, 3), -15)
        self.assertEqual(calculator.multiply(-5, -3), 15)
        self.assertEqual(calculator.multiply(0, 10), 0)
        self.assertAlmostEqual(calculator.multiply(2.5, 2), 5.0)
        self.assertEqual(calculator.mul(4, 3), 12)

    def test_divide(self):
        self.assertEqual(calculator.divide(2, 10), 5)
        self.assertEqual(calculator.divide(-2, 10), -5)
        self.assertEqual(calculator.divide(4, -12), -3)
        self.assertAlmostEqual(calculator.divide(2, 7), 3.5)
        self.assertEqual(calculator.div(2, 10), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(0, 10)

        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(calculator.logarithm(2, 8), 3)
        self.assertAlmostEqual(calculator.logarithm(10, 100), 2)
        self.assertAlmostEqual(calculator.logarithm(3, 27), 3)
        self.assertAlmostEqual(calculator.logarithm(0.5, 8), -3)
        self.assertAlmostEqual(calculator.log(2, 16), 4)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(2, 0)

        with self.assertRaises(ValueError):
            calculator.logarithm(2, -8)

        with self.assertRaises(ValueError):
            calculator.log(10, 0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 8)

        with self.assertRaises(ValueError):
            calculator.logarithm(0, 8)

        with self.assertRaises(ValueError):
            calculator.logarithm(-2, 8)

    # Partner 2 tests

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5)
        self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13)
        self.assertAlmostEqual(calculator.hypotenuse(0, 5), 5)
        self.assertAlmostEqual(calculator.hypotenuse(1, 1), 2 ** 0.5)

    def test_sqrt(self):
        self.assertAlmostEqual(calculator.square_root(25), 5)
        self.assertAlmostEqual(calculator.square_root(0), 0)
        self.assertAlmostEqual(calculator.square_root(2), 2 ** 0.5)

        with self.assertRaises(ValueError):
            calculator.square_root(-4)

        with self.assertRaises(ValueError):
            calculator.square_root(-0.1)

    # Additional tests

    def test_exponent(self):
        self.assertEqual(calculator.exponent(2, 3), 8)
        self.assertEqual(calculator.exponent(5, 0), 1)
        self.assertEqual(calculator.exponent(2, -2), 0.25)
        self.assertEqual(calculator.exponent(-2, 3), -8)
        self.assertEqual(calculator.exp(3, 2), 9)

    def test_negative_hypotenuse_inputs(self):
        self.assertAlmostEqual(calculator.hypotenuse(-3, -4), 5)
        self.assertAlmostEqual(calculator.hypotenuse(-3, 4), 5)


if __name__ == "__main__":
    unittest.main()
