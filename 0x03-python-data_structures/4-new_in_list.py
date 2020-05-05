#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """ a = my_list.copy() """
    a = my_list[:]
    if idx >= 0 and idx < len(my_list):
        a[idx] = element
    return (a)
