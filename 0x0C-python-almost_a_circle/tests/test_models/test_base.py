#!/usr/bin/python3
"""Unittest for class base([..])
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
        """class"""
        def test_none(self):
                """none"""
                with self.assertRaises(TypeError) as e:
                        msg = "__init__() missing 1 required positional \
argument: 'self'"
                        Base.__init__()
                self.assertEqual(msg, str(e.exception))

        def test_no_args(self):
                """test without args"""
                b1 = Base()
                b2 = Base()
                self.assertEqual(b1.id, b2.id - 1)
                self.assertEqual(b1.__dict__, {"id": b1.id})
                self.assertTrue(hasattr(b1, "id"))
                self.assertTrue(hasattr(b1, '_Base__nb_objects'))

        def test_one_arg(self):
                """one arg"""
                b1 = Base(5)
                b2 = Base(10)
                self.assertEqual(b1.id, 5)
                self.assertEqual(b2.id, 10)

        def test_two_args(self):
                """two args"""
                with self.assertRaises(TypeError) as e:
                        msg = "__init__() takes from 1 to 2 positional arguments \
but 3 were given"
                        b1 = Base(5, 10)
                self.assertEqual(msg, str(e.exception))
                b1 = Base()

        def test_dict_to_json_string(self):
                """dict to json string"""
                r1 = Rectangle(10, 7, 2, 8, 5)
                d = r1.to_dictionary()
                jd = Base.to_json_string([d])
                s = '[{"x": 2, "width": 10, "id": 5, "height": 7, "y": 8}]'
                self.assertEqual(print(jd), print(s))
                self.assertEqual(str(type(jd)), "<class 'str'>")
                jd = Base.to_json_string([None])
                self.assertEqual(print(jd), print("[]"))

        def test_savetofile(self):
                """save to file"""
                r1 = Rectangle(10, 7, 2, 8)
                r2 = Rectangle(2, 4)
                Rectangle.save_to_file([r1, r2])
                s = '[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}, \
{"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]'
                with open("Rectangle.json", "r") as f:
                        self.assertEqual(print(f.read()), print(s))
                        Rectangle.save_to_file([r1, r2])
                        self.assertEqual(print(f.read()), print("[]"))

        def test_from_json_string(self):
                """from json string"""
                list_input = [
                        {'id': 89, 'width': 10, 'height': 4},
                        {'id': 7, 'width': 1, 'height': 7}
                ]
                json_list_input = Rectangle.to_json_string(list_input)
                list_output = Rectangle.from_json_string(json_list_input)
                s = "[<class 'list'>] [{'height': 4, 'width': 10, 'id': 89}, \
{'height': 7, 'width': 1, 'id': 7}]"
                self.assertEqual(print("[{}] {}".format(type(list_output),
                                       list_output)),
                                 print(s))
                json_list_input = Rectangle.to_json_string(None)
                list_output = Rectangle.from_json_string(json_list_input)
                self.assertEqual(print("[{}] {}".format(type(list_output),
                                       list_output)),
                                 print("[]"))

        def test_create(self):
                """create"""
                r1 = Rectangle(3, 5, 1, 4, 5)
                r1_dictionary = r1.to_dictionary()
                r2 = Rectangle.create(**r1_dictionary)
                self.assertAlmostEqual(print(r1), print(r2))
                self.assertFalse(r1 is r2)
                self.assertFalse(r1 == r2)

        def test_load_from_file(self):
                """load from file"""
                r1 = Rectangle(10, 7, 2, 8)
                r2 = Rectangle(2, 4)
                list_rectangles_input = [r1, r2]
                Rectangle.save_to_file(list_rectangles_input)
                list_rectangles_output = Rectangle.load_from_file()
                self.assertEqual(print(list_rectangles_output[0]), print(r1))
                self.assertEqual(print(list_rectangles_output[1]), print(r2))
                s1 = Square(5)
                s2 = Square(7, 9, 1)
                list_squares_input = [s1, s2]

                Square.save_to_file(list_squares_input)

                lso = Square.load_from_file()
                self.assertEqual(print(lso[0]), print(s1))
                self.assertEqual(print(lso[1]), print(s2))

if __name__ == '__main__':
    unittest.main()
