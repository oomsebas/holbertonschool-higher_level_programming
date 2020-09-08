#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cpy_list = []

    lent = len(my_list)
    cpy_list = my_list.copy()
    if my_list is None and element is none:
        return (cpy_list)
    if idx < 0 or idx > lent:
        return (cpy_list)
    else:
        cpy_list[idx] = element
        return (cpy_list)
