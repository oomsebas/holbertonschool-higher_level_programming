#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    lent = len(my_list)

    if idx < 0:
        return (my_list)
    if idx < lent:
        my_list[idx] = element
        return (my_list)
    else:
        return(my_list)
