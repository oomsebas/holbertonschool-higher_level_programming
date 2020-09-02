#!/usr/bin/python3
def pow(a, b):

    if (b == 0):
        return 1
    if b > 0:
        c = 1
        for i in range(b):
            c = c * a
    else:
        c = 1
        for i in range(abs(b)):
            c = c / a

    return c
