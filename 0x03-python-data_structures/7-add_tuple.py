#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tup = tuple((tuple_a, tuple_b))
    tup1 = 0
    tup2 = 0

    for enum, i in enumerate(tup):
        for enum1, j in enumerate(i):
            if enum1 == 0:
                tup1 = tup1 + j
            else:
                tup2 = tup2 + j

    return (tup1, tup2)
