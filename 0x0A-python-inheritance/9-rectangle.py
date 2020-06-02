#!/usr/bin/python3
"""Module.



"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        returns the area of a rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        x = str(self.__class__.__name__)
        return "[" + x + "] " + str(self.__width) + "/" + str(self.__height)
