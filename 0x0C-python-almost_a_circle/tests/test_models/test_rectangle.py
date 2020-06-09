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
                self.assertEqual(r1.width, 10)
                self.assertEqual(r1.height, 12)
                self.assertEqual(r1.area(), 120)

        def test_three_args(self):
                """two args"""
                r1 = Rectangle(10, 2, 12)
                r2 = Rectangle(10, 2, 3)
                self.assertEqual(r1.id, r2.id - 1)
                self.assertEqual(r1.width, 10)
                self.assertEqual(r1.height, 2)
                self.assertEqual(r1.x, 12)
                self.assertEqual(r1.area(), 20)
                self.assertTrue(hasattr(r1, "id"))
                self.assertTrue(hasattr(r1, '_Base__nb_objects'))

        def test_four_args(self):
                """two args"""
                r1 = Rectangle(10, 2, 0, 0)
                r2 = Rectangle(10, 2, 0, 7)
                self.assertEqual(r1.id, r2.id - 1)
                self.assertEqual(r1.width, 10)
                self.assertEqual(r1.height, 2)
                self.assertEqual(r1.x, 0)
                self.assertEqual(r1.y, 0)

        def test_five_args(self):
                """two args"""
                r1 = Rectangle(10, 2, 12, 10, 5)
                r2 = Rectangle(10, 2, 3, 4, 9)
                self.assertEqual(r1.id, 5)
                self.assertEqual(r2.id, 9)
                self.assertEqual(r1.width, 10)
                self.assertEqual(r1.height, 2)
                self.assertEqual(r1.x, 12)
                self.assertEqual(r1.y, 10)
                self.assertEqual(r1.area(), 20)
                self.assertEqual(r1.__dict__, {'id': 5,
                                               '_Rectangle__width': 10,
                                               '_Rectangle__height': 2,
                                               '_Rectangle__x': 12,
                                               '_Rectangle__y': 10})

        def test_more_args(self):
                """two args"""
                with self.assertRaises(TypeError):
                        r1 = Rectangle(10, 2, 12, 10, 5, 4)

        def test_type_args(self):
                """ types"""
                with self.assertRaises(TypeError) as e:
                        ex = "width must be an integer"
                        r1 = Rectangle("a", 5)
                self.assertEqual(ex, str(e.exception))
                with self.assertRaises(TypeError) as e:
                        ex = "height must be an integer"
                        r1 = Rectangle(5, "a")
                self.assertEqual(ex, str(e.exception))
                with self.assertRaises(ValueError) as e:
                        ex = "x must be >= 0"
                        r1 = Rectangle(5, 5, -4, 4)
                self.assertEqual(ex, str(e.exception))
                with self.assertRaises(ValueError) as e:
                        ex = "y must be >= 0"
                        r1 = Rectangle(5, 5, 5, -5)
                self.assertEqual(ex, str(e.exception))
                with self.assertRaises(TypeError):
                        r1 = Rectangle(5, 5, "x", -5)
                with self.assertRaises(TypeError):
                        r1 = Rectangle(5, 5, "y", -5)

        def test_display(self):
                """display"""
                r1 = Rectangle(1, 2)
                dis = "#\n#\n"
                self.assertEqual(r1.display(), print(dis))

        def test_inheritance(self):
                """inheritance"""
                r1 = Rectangle(10, 5)
                self.assertTrue(issubclass(Rectangle, Base))
                self.assertTrue(isinstance(r1, Base))

        def test_str(self):
                """str"""
                r1 = Rectangle(10, 10, 10, 10)
                s = "[Rectangle] (1) 10/10 - 10/10"
                self.assertEqual(print(s), print(r1))
                r1.update(89)
                s = "[Rectangle] (89) 10/10 - 10/10"
                self.assertEqual(print(s), print(r1))
                r1.update(89, 2)
                s = "[Rectangle] (89) 10/10 - 2/10"
                self.assertEqual(print(s), print(r1))
                r1.update(89, 2, 3)
                s = "[Rectangle] (89) 10/10 - 2/3"
                self.assertEqual(print(s), print(r1))
                r1.update(89, 2, 3, 4)
                s = "[Rectangle] (89) 4/10 - 2/3"
                self.assertEqual(print(s), print(r1))
                r1.update(89, 2, 3, 4, 5)
                s = "[Rectangle] (89) 4/10 - 2/3"
                self.assertEqual(print(s), print(r1))

        def test_kwargs(self):
                """kwargs"""
                r1 = Rectangle(10, 10, 10, 10)
                s = "[Rectangle] (1) 10/10 - 10/10"
                self.assertEqual(print(r1), print(s))

                r1.update(height=1)
                s = "[Rectangle] (1) 10/10 - 10/1"
                self.assertEqual(print(r1), print(s))

                r1.update(width=1, x=2)
                s = "[Rectangle] (1) 2/10 - 1/1"
                self.assertEqual(print(r1), print(s))

                r1.update(y=1, width=2, x=3, id=89)
                s = "[Rectangle] (89) 3/1 - 2/1"
                self.assertEqual(print(r1), print(s))

                r1.update(x=1, height=2, y=3, width=4)
                s = "[Rectangle] (89) 1/3 - 4/2"
                self.assertEqual(print(r1), print(s))


if __name__ == '__main__':
    unittest.main()
