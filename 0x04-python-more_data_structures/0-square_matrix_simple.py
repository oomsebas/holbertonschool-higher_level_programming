#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    x = []
    for b in matrix:
        x.append(list(map(lambda x: x * x, b)))
    return x
