#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cpy_list = []

    lent = len(my_list)
    cpy_list = my_list.copy()

    if idx < lent and idx >= 0:
        cpy_list[idx] = element
        return (cpy_list)
    else:
        return (cpy_list)
