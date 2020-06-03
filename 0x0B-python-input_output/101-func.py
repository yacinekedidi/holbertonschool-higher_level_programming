#!/usr/bin/python3
"""Module.


"""


def print_stat(s, d):
    """
    print the stats and size.
    """
    print("File size: {:d}".format(s))
    for k, v in d.items():
        print("{}: {:d}".format(k, v))
