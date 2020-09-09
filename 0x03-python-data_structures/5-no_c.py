#!/usr/bin/python3
def no_c(my_string):
    cpy = ""

    for num, letter in enumerate(my_string):
        if letter not in 'cC':
            cpy = cpy + letter
    return cpy
