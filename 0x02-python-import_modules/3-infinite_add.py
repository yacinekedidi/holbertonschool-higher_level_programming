#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    l = len(sys.argv)
    sum = 0
    for i in range(1, l):
        sum += int(sys.argv[i])
    print("{}".format(sum))
