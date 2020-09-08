#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cpy_list = []

    lent = len(my_list)
    cpy_list = my_list.copy()
    if my_list is None or element is None:
        return
    if idx < lent:
        cpy_list[idx] = element
        return (cpy_list)
    else:
        return (cpy_list)
