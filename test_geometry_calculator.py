"""
Unit tests for the geometry_calculator module.
"""

import math
import unittest

from geometry_calculator import (
    circle_area,
    circle_perimeter,
    rectangle_area,
    rectangle_perimeter,
    trapezoid_area,
    triangle_area,
    triangle_perimeter,
)


class TestCircleArea(unittest.TestCase):
    def test_positive_radius(self):
        self.assertAlmostEqual(circle_area(5), math.pi * 25)

    def test_zero_radius(self):
        self.assertEqual(circle_area(0), 0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            circle_area(-1)


class TestCirclePerimeter(unittest.TestCase):
    def test_positive_radius(self):
        self.assertAlmostEqual(circle_perimeter(5), 2 * math.pi * 5)

    def test_zero_radius(self):
        self.assertEqual(circle_perimeter(0), 0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            circle_perimeter(-3)


class TestRectangleArea(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(rectangle_area(4, 6), 24)

    def test_zero_side(self):
        self.assertEqual(rectangle_area(0, 5), 0)

    def test_negative_width(self):
        with self.assertRaises(ValueError):
            rectangle_area(-1, 5)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            rectangle_area(4, -2)


class TestRectanglePerimeter(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(rectangle_perimeter(4, 6), 20)

    def test_zero_side(self):
        self.assertEqual(rectangle_perimeter(0, 5), 10)

    def test_negative_value(self):
        with self.assertRaises(ValueError):
            rectangle_perimeter(-1, 5)


class TestTriangleArea(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(triangle_area(3, 8), 12)

    def test_zero_base(self):
        self.assertEqual(triangle_area(0, 5), 0)

    def test_negative_base(self):
        with self.assertRaises(ValueError):
            triangle_area(-2, 5)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            triangle_area(3, -4)


class TestTrianglePerimeter(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(triangle_perimeter(3, 4, 5), 12)

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            triangle_perimeter(1, 2, 10)

    def test_zero_side(self):
        with self.assertRaises(ValueError):
            triangle_perimeter(0, 4, 5)

    def test_negative_side(self):
        with self.assertRaises(ValueError):
            triangle_perimeter(-1, 4, 5)


class TestTrapezoidArea(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(trapezoid_area(4, 6, 5), 25)

    def test_zero_height(self):
        self.assertEqual(trapezoid_area(4, 6, 0), 0)

    def test_negative_base(self):
        with self.assertRaises(ValueError):
            trapezoid_area(-1, 6, 5)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            trapezoid_area(4, 6, -3)


if __name__ == "__main__":
    unittest.main()
