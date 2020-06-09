#!/usr/bin/python3
"""Module.




"""
from models.base import Base


class Rectangle(Base):
    """
    subclass.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.integer_validator("y", value)
        self.__y = value

    def integer_validator(self, name, value):
        """
        function.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if name in ["width", "height"]:
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        if name in ["x", "y"]:
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """
        Function.
        """
        return self.__width * self.__height

    def display(self):
        """
        Function.
        """
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__width + self.__x):
                if j < self.__x:
                    print(" ", end="")
                else:
                    print("#", end="")
            print()

    def __str__(self):
        x = self.__class__.__name__
        if x == "Rectangle":
            return "[{}] ({}) {}/{} - {}/{}".format(x, self.id,
                                                    self.__x, self.__y,
                                                    self.__width,
                                                    self.__height)
        else:
            return "[{}] ({}) {}/{} - {}".format(x,
                                                 self.id, self.__x,
                                                 self.__y, self.__width)

    def update(self, *args, **kwargs):
        """
        updates attribute instances.
        """
        if args:
            for i, ar in enumerate(args):
                if i == 0:
                    self.id = ar
                elif i == 1:
                    self.width = ar
                elif i == 2:
                    self.height = ar
                elif i == 3:
                    self.x = ar
                elif i == 4:
                    self.y = ar
        elif kwargs:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """
        dict repr of Rectangle.
        """
        return {'id': self.id, 'width': self.__width, 'height': self.__height,
                'x': self.__x, 'y': self.__y}
