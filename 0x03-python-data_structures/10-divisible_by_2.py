#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if (my_list is None) or (len(my_list) < 1):
        return None
    cpy = []
    cpy = my_list.copy()
    for enum, num in enumerate(my_list):
        if num % 2 == 0:
            cpy[enum] = True
        else:
            cpy[enum] = False
    return cpy
