#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    big = my_list[0]
""" my_list.sort() """
    for i in range(0,len(my_list)):
        if my_list[i] > big:
            big = my_list[i]
        i += 1
    return (big)
