#!/usr/bin/python3
"""Unittest for class base([..])
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
        """class"""

        def test_no_args(self):
                """test without args"""
                b1 = Square(5)
                b2 = Square(5)
                self.assertEqual(b1.id, b2.id - 1)

if __name__ == '__main__':
    unittest.main()
