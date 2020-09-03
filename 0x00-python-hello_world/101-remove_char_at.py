#!/usr/bin/python3
def remove_char_at(str, n):
    cpy = ""
    for num, i in enumerate(str):
        if num != n:
            cpy = cpy + i
    return (cpy)
