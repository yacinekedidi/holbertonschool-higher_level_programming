#!/usr/bin/python3
def weight_average(my_list=[]):
    if (len(my_list) == 0):
        return 0
    sum = 0
    size = 0
    for i in my_list:
        sum += i[1] * i[0]
        size += i[1]
    return (sum / size)
