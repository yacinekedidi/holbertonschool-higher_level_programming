#!/usr/bin/python3
"""Unittest for class base([..])
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square



class TestBase(unittest.TestCase):

	def setUp(self):
		"""instantiates class"""
		Base._Base__nb_objects = 0
		pass

	def tearDown(self):
		"""after each test method cleans up"""
		pass

	def test_no_args(self):
		"""test without args"""
		self.assertEqual(Base._Base__nb_objects, 0)
		b1 = Base()
		b2 = Base()
		self.assertEqual(b1.id, b2.id - 1)
		self.assertEqual(b1._Base__nb_objects, 2)

if __name__ == '__main__':
    unittest.main()
