#!/usr/bin/python3
def max_integer(my_list=[]):
    max = my_list[0]

    if (my_list is None) or (len(my_list) < 1):
        return
    for num in my_list:
        if num > max:
            max = num
    return max
