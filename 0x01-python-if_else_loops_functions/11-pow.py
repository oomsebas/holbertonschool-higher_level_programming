#!/usr/bin/python3
def pow(a, b):
    c = 1
    if (b == 0):
        return 1
    if (a == 0 and b < 0):
        return
    if b > 0:
        for i in range(b):
            c = c * a
    else:
        for i in range(abs(b)):
            c = c / a
    return c
