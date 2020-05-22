#!/usr/bin/python3
"""module matrix_divide.



"""


def matrix_mul(m_a, m_b):
    """
    function matrix_mul
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if any(not isinstance(i, list) for i in m_a):
        raise TypeError("m_a must be a list of lists")

    if any(not isinstance(i, list) for i in m_b):
        raise TypeError("m_b must be a list of lists")

    if not m_a or any(not i for i in m_a):
        raise ValueError("m_a can't be empty")
    if not m_b or any(not i for i in m_b):
        raise ValueError("m_b can't be empty")

    if any(not isinstance(i, (int, float)) for a in m_a for i in a):
        raise TypeError("m_a should contain only integers or floats")
    if any(not isinstance(i, (int, float)) for a in m_b for i in a):
        raise TypeError("m_b should contain only integers or floats")

    if any(len(m_a[0]) != len(x) for x in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if any(len(m_b[0]) != len(x) for x in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    r = [[] for i in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            x = 0
            for k in range(len(m_b)):
                x += m_a[i][k] * m_b[k][j]
            r[i].append(x)
    return (r)
