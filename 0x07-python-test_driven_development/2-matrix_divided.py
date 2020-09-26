#!/usr/bin/python3
""" script for task 1, we define a subroutine that divides a matrix"""


def matrix_divided(matrix, div):
    """function that divides a matrix

    Args:
    matrix(list): Matrix to be divided
    div(int): Number to divide

    Return:
    the matrix divided
    """
    if matrix is None or len(matrix) is 0:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    new_matrix = []
    check_float_int(matrix)
    check_lenrow(matrix)
    check_divider(div)
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]
    return (new_matrix)


def check_float_int(matrix):
    """function that checks for the members of the matrix
    is not int or float"""
    for row in matrix:
        if type(row) is not list or len(row) is 0:
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
            break
        for num in row:
            if type(num) in (int, float):
                continue
            else:
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')


def check_lenrow(matrix):
    """function that check the lenghts of the rows"""
    equal = []
    for row in matrix:
        equal.append(len(row))
    if len(set(equal)) != 1 and len(equal) > 1:
        raise TypeError('Each row of the matrix must have the same size')


def check_divider(div):
    """function that check the divisor"""
    if type(div) not in (int, float) or div is None:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError('division by zero')
