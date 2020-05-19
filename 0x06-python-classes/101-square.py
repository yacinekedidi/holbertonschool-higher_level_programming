#!/usr/bin/python3
"""Square class."""


class Square:
    """defines a square."""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def __str__(self):
        return self.my_Strprint()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) != 2 or not isinstance(value[0], int) or\
           not isinstance(value[1], int) or value[0] < 0 or\
           value[1] < 0 or not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_Strprint(self):
        my_str = ""
        if self.__size == 0:
            return "\n"
        else:
            for i in range(self.__position[1]):
                my_str += "\n"
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    my_str += " "
                for x in range(self.__size):
                    my_str += "#"
                my_str += "\n"
        return my_str[:-1]

    def my_print(self):
        print(self.my_Strprint())
