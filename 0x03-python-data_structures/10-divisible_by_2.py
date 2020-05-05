#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    lst = my_list.copy()
    for i in range(len(my_list)):
        lst[i] = True if my_list[i] % 2 == 0 else False
    return (lst)
