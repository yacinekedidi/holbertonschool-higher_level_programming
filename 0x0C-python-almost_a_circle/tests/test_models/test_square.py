#!/usr/bin/python3
"""Unittest for class base([..])
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
        """class"""
        def test_no_args(self):
                """test without args"""
                with self.assertRaises(TypeError):
                        Square()

        def test_one_arg(self):
                """one arg"""
                r1 = Square(10)
                r2 = Square(12)
                self.assertEqual(r1.id, r2.id - 1)
                self.assertEqual(r1.size, 10)

        def test_two_args(self):
                """two args"""
                r1 = Square(10, 12)
                r2 = Square(10, 2)
                self.assertEqual(r1.id, r2.id - 1)
                self.assertEqual(r1.size, 10)
                self.assertEqual(r1.x, 12)

        def test_three_args(self):
                """two args"""
                r1 = Square(10, 2, 12)
                r2 = Square(10, 2, 3)
                self.assertEqual(r1.id, r2.id - 1)
                self.assertEqual(r1.size, 10)
                self.assertEqual(r1.x, 2)
                self.assertEqual(r1.y, 12)

        def test_four_args(self):
                """two args"""
                r1 = Square(10, 2, 12, 6)
                r2 = Square(10, 2, 0, 7)
                self.assertEqual(r1.size, 10)
                self.assertEqual(r1.x, 2)
                self.assertEqual(r1.y, 12)
                self.assertEqual(r1.id, 6)
                self.assertEqual(r2.id, 7)

        def test_more(self):
                """two args"""
                with self.assertRaises(TypeError):
                        r1 = Square(10, 2, 12, 10, 5)


if __name__ == '__main__':
    unittest.main()
