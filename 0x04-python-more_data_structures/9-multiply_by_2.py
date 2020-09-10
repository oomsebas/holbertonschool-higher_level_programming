#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    cpy_res = {k: v * 2 for k, v in a_dictionary.items()}
    return cpy_res
