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
                self.assertEqual(r1.area(), 100)
                """dict = {'id': 13, '_Rectangle__width': 10,
                        '_Rectangle__height': 10,
                        '_Rectangle__x': 0,'_Rectangle__y': 0}
                self.assertEqual(r1.__dict__, dict)"""
                self.assertTrue(hasattr(r1, "id"))
                self.assertTrue(hasattr(r1, '_Base__nb_objects'))

        def test_two_args(self):
                """two args"""
                r1 = Square(10, 12)
                r2 = Square(10, 2)
                self.assertEqual(r1.id, r2.id - 1)
                self.assertEqual(r1.size, 10)
                self.assertEqual(r1.x, 12)
                self.assertEqual(r1.area(), 100)

        def test_three_args(self):
                """two args"""
                r1 = Square(10, 2, 12)
                r2 = Square(10, 2, 3)
                self.assertEqual(r1.id, r2.id - 1)
                self.assertEqual(r1.size, 10)
                self.assertEqual(r1.x, 2)
                self.assertEqual(r1.y, 12)
                self.assertEqual(r1.area(), 100)

        def test_four_args(self):
                """two args"""
                r1 = Square(10, 2, 12, 6)
                r2 = Square(10, 2, 0, 7)
                self.assertEqual(r1.size, 10)
                self.assertEqual(r1.x, 2)
                self.assertEqual(r1.y, 12)
                self.assertEqual(r1.id, 6)
                self.assertEqual(r2.id, 7)
                self.assertEqual(r1.area(), 100)

        def test_more(self):
                """two args"""
                with self.assertRaises(TypeError):
                        r1 = Square(10, 2, 12, 10, 5)

        def test_type_args(self):
                """ types"""
                with self.assertRaises(TypeError) as e:
                        ex = "width must be an integer"
                        r1 = Square("a", 5)
                self.assertEqual(ex, str(e.exception))
                with self.assertRaises(ValueError) as e:
                        ex = "x must be >= 0"
                        r1 = Square(5, -4, 4)
                self.assertEqual(ex, str(e.exception))
                with self.assertRaises(ValueError) as e:
                        ex = "y must be >= 0"
                        r1 = Square(5, 5, -5)
                self.assertEqual(ex, str(e.exception))
                with self.assertRaises(TypeError):
                        r1 = Square(5, "x", 0)
                with self.assertRaises(TypeError):
                        r1 = Square(5, "y", 0)

        def test_display(self):
                """display"""
                r1 = Square(2)
                dis = "##\n##\n"
                self.assertEqual(r1.display(), print(dis))
                r1 = Square(2, 1, 2)
                dis = "\n\n ##\n ##\n"
                self.assertEqual(r1.display(), print(dis))

        def test_inheritance(self):
                """inheritance"""
                r1 = Square(10, 5)
                self.assertTrue(issubclass(Square, Base))
                self.assertTrue(isinstance(r1, Base))

if __name__ == '__main__':
    unittest.main()
