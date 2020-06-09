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

        def test_main(self):
                """test without args"""
                b1 = Base()
                self.assertEqual(b1.id, 1)

                b2 = Base()
                self.assertEqual(b2.id, 2)

                b3 = Base()
                self.assertEqual(b3.id, 3)

                b4 = Base(12)
                self.assertEqual(b4.id, 12)

                b5 = Base()
                self.assertEqual(b5.id, 4)
if __name__ == '__main__':
    unittest.main()
