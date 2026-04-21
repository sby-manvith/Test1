"""
Unit tests for the calculator module.
"""

import unittest
from calculator import add, subtract, multiply, divide, power, factorial, is_prime, square_root


class TestAdd(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(3, 5), 8)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_mixed_sign(self):
        self.assertEqual(add(-4, 7), 3)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(5, 0), 5)

    def test_add_floats(self):
        self.assertAlmostEqual(add(1.1, 2.2), 3.3, places=5)


class TestSubtract(unittest.TestCase):
    def test_subtract_positive_numbers(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_subtract_resulting_negative(self):
        self.assertEqual(subtract(3, 7), -4)

    def test_subtract_zero(self):
        self.assertEqual(subtract(5, 0), 5)

    def test_subtract_same_values(self):
        self.assertEqual(subtract(9, 9), 0)


class TestMultiply(unittest.TestCase):
    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(6, 7), 42)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(100, 0), 0)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(-3, -4), 12)

    def test_multiply_mixed_sign(self):
        self.assertEqual(multiply(-5, 3), -15)

    def test_multiply_floats(self):
        self.assertAlmostEqual(multiply(2.5, 4.0), 10.0, places=5)


class TestDivide(unittest.TestCase):
    def test_divide_even(self):
        self.assertEqual(divide(15, 3), 5.0)

    def test_divide_returns_float(self):
        self.assertAlmostEqual(divide(1, 3), 0.3333, places=3)

    def test_divide_negative(self):
        self.assertEqual(divide(-10, 2), -5.0)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ValueError):
            divide(5, 0)

    def test_divide_floats(self):
        self.assertAlmostEqual(divide(7.5, 2.5), 3.0, places=5)


class TestPower(unittest.TestCase):
    def test_power_positive_exponent(self):
        self.assertEqual(power(2, 10), 1024)

    def test_power_zero_exponent(self):
        self.assertEqual(power(5, 0), 1)

    def test_power_one_exponent(self):
        self.assertEqual(power(7, 1), 7)

    def test_power_negative_exponent(self):
        self.assertAlmostEqual(power(2, -1), 0.5, places=5)

    def test_power_fractional_exponent(self):
        self.assertAlmostEqual(power(9, 0.5), 3.0, places=5)


class TestFactorial(unittest.TestCase):
    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_one(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_five(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_ten(self):
        self.assertEqual(factorial(10), 3628800)

    def test_factorial_negative_raises(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_factorial_non_integer_raises(self):
        with self.assertRaises(TypeError):
            factorial(3.5)


class TestIsPrime(unittest.TestCase):
    def test_prime_small(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))

    def test_prime_large(self):
        self.assertTrue(is_prime(97))
        self.assertTrue(is_prime(101))

    def test_not_prime(self):
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(15))

    def test_not_prime_zero(self):
        self.assertFalse(is_prime(0))

    def test_non_integer_raises(self):
        with self.assertRaises(TypeError):
            is_prime(3.5)


class TestSquareRoot(unittest.TestCase):
    def test_square_root_perfect_square(self):
        self.assertEqual(square_root(25), 5.0)

    def test_square_root_zero(self):
        self.assertEqual(square_root(0), 0.0)

    def test_square_root_non_perfect(self):
        self.assertAlmostEqual(square_root(2), 1.41421, places=5)

    def test_square_root_negative_raises(self):
        with self.assertRaises(ValueError):
            square_root(-1)


if __name__ == "__main__":
    unittest.main()
