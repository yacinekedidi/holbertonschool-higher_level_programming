#!/usr/bin/python3
"""Module.


"""


def print_stat(s, d):
    """
    print the stats and size.
    """
    print("File size: {}".format(s))
    for k, v in d.items():
        if v != 0:
            print("{}: {}".format(k, v))
