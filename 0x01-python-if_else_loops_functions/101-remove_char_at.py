#!/usr/bin/python3
def remove_char_at(str, n):
    x = 0
    str1 = ""
    for i in str:
        if x != n:
            str1 += i
        x += 1
    return str1
