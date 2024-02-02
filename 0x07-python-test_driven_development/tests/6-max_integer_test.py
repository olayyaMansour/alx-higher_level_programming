#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_regular_list(self):
        """Test regular list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test unordered list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test empty list."""
        self.assertEqual(max_integer([]), None)

    def test_single_element_list(self):
        """Test single element list."""
        self.assertEqual(max_integer([42]), 42)

    def test_negative_numbers(self):
        """Test list with negative numbers."""
        self.assertEqual(max_integer([-1, -5, -2]), -1)

    def test_float_numbers(self):
        """Test list with float numbers."""
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)

    def test_mixed_data_types(self):
        """Test list with mixed data types."""
        self.assertEqual(max_integer([1, "string", 3]), None)
