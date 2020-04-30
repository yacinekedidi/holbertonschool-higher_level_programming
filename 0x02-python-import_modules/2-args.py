#!/usr/bin/python3
import sys
if __name__ == "__main__":
    l = len(sys.argv)
    if l == 1:
        print("0 arguments.")
    elif l == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(l - 1))
    for i in range(1, l):
        print("{}: {}".format(i, sys.argv[i]))
