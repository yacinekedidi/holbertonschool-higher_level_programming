#!/usr/bin/python3
"""Module



"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    subclass
    """
    def __init__(self, size):
        super().__init__(size, size)
        self.size = size
