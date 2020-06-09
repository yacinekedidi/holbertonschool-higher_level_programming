#!/usr/bin/python3
"""Unittest for class base([..])
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
        """class"""
        def test_no_args(self):
                """test without args"""
                b1 = Base()
                b2 = Base()
                self.assertEqual(b1.id, b2.id - 1)

        def test_one_arg(self):
                """one arg"""
                b1 = Base(5)
                b2 = Base(10)
                self.assertEqual(b1.id, 5)
                self.assertEqual(b2.id, 10)

        def test_two_args(self):
                """two args"""
                with self.assertRaises(TypeError):
                        b1 = Base(5, 10)

if __name__ == '__main__':
    unittest.main()
