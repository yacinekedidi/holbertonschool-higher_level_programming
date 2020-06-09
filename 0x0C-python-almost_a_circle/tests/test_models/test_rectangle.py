#!/usr/bin/python3
"""Unittest for class base([..])
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle_instantiation(unittest.TestCase):
        """class"""
        def test_no_args(self):
                """test without args"""
                with self.assertRaises(TypeError):
                        Rectangle()

        def test_one_arg(self):
                """one arg"""
                with self.assertRaises(TypeError):
                        r1 = Rectangle(10)

        def test_two_args(self):
                """two args"""
                r1 = Rectangle(10, 12)
                r2 = Rectangle(10, 2)
                self.assertEqual(r1.id, r2.id - 1)

        def test_three_args(self):
                """two args"""
                r1 = Rectangle(10, 2, 12)
                r2 = Rectangle(10, 2, 3)
                self.assertEqual(r1.id, r2.id - 1)

        def test_four_args(self):
                """two args"""
                r1 = Rectangle(10, 2, 12, 6)
                r2 = Rectangle(10, 2, 0, 7)
                self.assertEqual(r1.id, r2.id - 1)

        def test_five_args(self):
                """two args"""
                r1 = Rectangle(10, 2, 12, 10, 5)
                r2 = Rectangle(10, 2, 3, 4, 9)
                self.assertEqual(r1.id, 5)
                self.assertEqual(r2.id, 9)

        def test_more_args(self):
                """two args"""
                with self.assertRaises(TypeError):
                        r1 = Rectangle(10, 2, 12, 10, 5, 4)

if __name__ == '__main__':
    unittest.main()
