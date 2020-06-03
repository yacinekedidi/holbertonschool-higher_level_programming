#!/usr/bin/python3
"""Module.



"""
import sys
ps = __import__('101-func').print_stat


if __name__ == "__main__":
    d = {
        "200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0}
    s = 0
    nbl = 0
    try:
        for line in sys.stdin:
            if nbl == 10:
                ps(s, d)
                nbl = 1
            else:
                nbl += 1
            line = line.split()
            s += int(line[-1])
            for k, v in d.items():
                if k == line[-2]:
                    d[k] += 1
        ps(s, d)
    except KeyboardInterrupt:
        ps(s, d)
        raise
