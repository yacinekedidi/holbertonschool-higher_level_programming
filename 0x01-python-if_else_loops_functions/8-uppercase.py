#!/usr/bin/python3
def islower(c):
    if ord(c) > 96 and ord(c) < 123:
        return True
    else:
        return False


def uppercase(str):
    for i in str:
        if islower(i):
            print("{:c}".format(ord(i) - 32), end="")
        else:
            print("{:c}".format(ord(i)), end="")
    print("")
