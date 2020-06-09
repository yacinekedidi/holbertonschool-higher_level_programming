#!/usr/bin/python3
"""Unittest for class base([..])
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
        """class"""
        def setUp(self):
                """setup"""
                Base._base__nb_objects = 0
                pass

        def tearDown(self):
                """tears down"""
                pass

        def test_no_args(self):
                """test without args"""
                b1 = Base()
                b2 = Base()
                self.assertEqual(b1.id, b2.id - 1)
                self.assertEqual(Base._Base__nb_objects, b2.id)
if __name__ == '__main__':
    unittest.main()
