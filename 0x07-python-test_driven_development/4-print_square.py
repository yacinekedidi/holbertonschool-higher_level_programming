#!/usr/bin/python3
"""module print_square."""


def print_square(size):
    """function print_square."""
    if type(size) not in [int, float]:
        raise TypeError("size must be an integer")
    if type(size) is int and size < 0:
        raise ValueError("size must be >= 0")

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    elif size > 0:
        size = int(size)
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
