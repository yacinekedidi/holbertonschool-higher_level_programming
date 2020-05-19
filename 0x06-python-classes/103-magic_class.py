"""MagicClass class."""
import math


class MagicClass:
    """defines a MagicClass."""
    def __init__(self, radius=0):
        self.radius = 0
        if type(radius) is not int and\
           type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        return self.__radius ** 2 * math.pi

    def circumference(self):
        return math.pi * 2 * self.__radius
