#!/usr/bin/python3
"""module for tests."""


import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMax_Integer(unittest.TestCase):
    def test_result(self):
        """test_result function."""
        self.assertEqual(max_integer([10, 20, 5]), 20)
        self.assertEqual(max_integer([20, 10, 5]), 20)
        self.assertEqual(max_integer([10, 10, 20]), 20)
        self.assertEqual(max_integer([20, 20, 20]), 20)
        self.assertEqual(max_integer([-10, -10, -10]), -10)
        self.assertEqual(max_integer([0.4, 5.5, 10.5]), 10.5)

    def test_errors(self):
        """test_errors functions."""
        self.assertRaises(TypeError, max_integer([100, "a", 5]))
