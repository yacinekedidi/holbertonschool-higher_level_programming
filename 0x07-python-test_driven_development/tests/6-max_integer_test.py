#!/usr/bin/python3
"""Unittest for max_integer([..])



"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_result(self):
        """
        test_result function.
        """
        self.assertEqual(max_integer([10, 20, 5]), 20)
        self.assertEqual(max_integer([20, 10, 5]), 20)
        self.assertEqual(max_integer([10, 10, 20]), 20)
        self.assertEqual(max_integer([20, 20, 20]), 20)
        self.assertEqual(max_integer([-10, -10, -10]), -10)
        self.assertEqual(max_integer([0.4, 5.5, 10.5]), 10.5)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([5]), 5)

    def test_errors(self):
        with self.assertRaises(TypeError):
            max_integer([10, "a", 5])

        with self.assertRaises(TypeError):
            max_integer(3)
        self.assertRaises(TypeError, max_integer, [0.5, "help"])

if __name__ == '__main__':
    unittest.main("tests/6-max_integer_test.py")
