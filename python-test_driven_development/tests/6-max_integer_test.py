#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_start(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-3, -2, -1]), -1)

    def test_mixed_signs(self):
        self.assertEqual(max_integer([-5, 0, 5]), 5)

    def test_floats(self):
        self.assertEqual(max_integer([1.1, 2.5, 3.9]), 3.9)

    def test_all_equal(self):
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_strings_in_list(self):
        self.assertEqual(max_integer(["a", "z", "c"]), "z")

    def test_string_input(self):
        self.assertEqual(max_integer("Holberton"), "t")

    def test_none_argument(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, "two", 3])
