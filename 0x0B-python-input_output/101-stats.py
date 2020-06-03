#!/usr/bin/python3
"""Module.



"""
import sys

def print_stat(s, d):
    """
    print the stats and size.
    """
    print("File size: {:d}".format(s))
    for k, v in d.items():
        print("{}: {:d}".format(k, v))


d = {"200": 0, "301": 0, "400" : 0, "401" : 0, "403" : 0, "404" : 0, "405" : 0, "500" : 0}
s = 0
nbl = 0
try:
    for line in sys.stdin:
        if nbl == 10:
            print_stat(s, d)
            nbl = 1
        else:
            nbl += 1
        line = line.split()
        s += int(line[-1])
        for k, v in d.items():
            if k == line[-2]:
                d[k] += 1
    print_stat(s, d)
except KeyboardInterrupt:
    print_stat(s, d)
