"""
Unit tests for the statistics_calculator module.
"""

import unittest
from statistics_calculator import mean, median, mode, variance, std_deviation


class TestMean(unittest.TestCase):
    def test_mean_integers(self):
        self.assertEqual(mean([1, 2, 3, 4, 5]), 3.0)

    def test_mean_single_element(self):
        self.assertEqual(mean([7]), 7.0)

    def test_mean_floats(self):
        self.assertAlmostEqual(mean([1.5, 2.5, 3.0]), 7.0 / 3, places=5)

    def test_mean_negative_numbers(self):
        self.assertEqual(mean([-1, -2, -3]), -2.0)

    def test_mean_empty_raises(self):
        with self.assertRaises(ValueError):
            mean([])

    def test_mean_non_list_raises(self):
        with self.assertRaises(TypeError):
            mean((1, 2, 3))


class TestMedian(unittest.TestCase):
    def test_median_odd_count(self):
        self.assertEqual(median([3, 1, 4, 1, 5]), 3)

    def test_median_even_count(self):
        self.assertEqual(median([1, 2, 3, 4]), 2.5)

    def test_median_single_element(self):
        self.assertEqual(median([42]), 42)

    def test_median_sorted_input(self):
        self.assertEqual(median([1, 2, 3, 4, 5]), 3)

    def test_median_unsorted_input(self):
        self.assertEqual(median([5, 3, 1, 4, 2]), 3)

    def test_median_empty_raises(self):
        with self.assertRaises(ValueError):
            median([])

    def test_median_non_list_raises(self):
        with self.assertRaises(TypeError):
            median("1 2 3")


class TestMode(unittest.TestCase):
    def test_mode_single_mode(self):
        self.assertEqual(mode([1, 2, 2, 3]), 2)

    def test_mode_multiple_modes_returns_smallest(self):
        self.assertEqual(mode([1, 1, 2, 2, 3]), 1)

    def test_mode_all_same(self):
        self.assertEqual(mode([5, 5, 5]), 5)

    def test_mode_single_element(self):
        self.assertEqual(mode([9]), 9)

    def test_mode_empty_raises(self):
        with self.assertRaises(ValueError):
            mode([])

    def test_mode_non_list_raises(self):
        with self.assertRaises(TypeError):
            mode({1, 2, 3})


class TestVariance(unittest.TestCase):
    def test_variance_known_value(self):
        self.assertAlmostEqual(variance([2, 4, 4, 4, 5, 5, 7, 9]), 4.0, places=5)

    def test_variance_single_element(self):
        self.assertEqual(variance([10]), 0.0)

    def test_variance_identical_elements(self):
        self.assertEqual(variance([3, 3, 3, 3]), 0.0)

    def test_variance_empty_raises(self):
        with self.assertRaises(ValueError):
            variance([])

    def test_variance_non_list_raises(self):
        with self.assertRaises(TypeError):
            variance(42)


class TestStdDeviation(unittest.TestCase):
    def test_std_deviation_known_value(self):
        self.assertAlmostEqual(std_deviation([2, 4, 4, 4, 5, 5, 7, 9]), 2.0, places=5)

    def test_std_deviation_single_element(self):
        self.assertEqual(std_deviation([10]), 0.0)

    def test_std_deviation_identical_elements(self):
        self.assertEqual(std_deviation([3, 3, 3, 3]), 0.0)

    def test_std_deviation_empty_raises(self):
        with self.assertRaises(ValueError):
            std_deviation([])

    def test_std_deviation_non_list_raises(self):
        with self.assertRaises(TypeError):
            std_deviation(None)


if __name__ == "__main__":
    unittest.main()
