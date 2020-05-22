#!/usr/bin/python3
"""module matrix_divided.



"""


def matrix_divided(matrix, div):
    """
    function matrix_divided
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    l = len(matrix[0])
    for i in matrix:
        if type(i) is not list:
            raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
        if len(i) != l:
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(i / div, 2) for i in j] for j in matrix]
