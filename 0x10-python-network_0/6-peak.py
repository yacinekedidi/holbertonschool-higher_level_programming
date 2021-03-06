#!/usr/bin/python3
"""Module"""


def find_peak(l):
    """function"""
    if len(l) == 0:
        return None
    if len(l) == 1:
        return l[0]
    if len(l) == 2:
        return max(l)

    if len(l) > 2:
        if l[0] >= l[1] and l[0] == max(l):
            return l[0]

    m = len(l) // 2
    if l[m] >= l[m - 1] and l[m] >= l[m + 1]:
        return l[m]
    return find_peak(l[m + 1:]) or find_peak(l[:m])
