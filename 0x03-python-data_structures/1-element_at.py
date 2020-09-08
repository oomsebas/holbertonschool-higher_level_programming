#!/usr/bin/python3
def element_at(my_list, idx):
    lent = len(my_list)
    if idx < 0:
        return None
    if idx < lent:
        return(my_list[idx])
    else:
        return None
