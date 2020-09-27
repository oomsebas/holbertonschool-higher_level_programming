#!/usr/bin/python3
"""matrix multiplication"""

def matrix_mul(m_a, m_b):
    """function that divides a matrix

    Args:
    m_a(list of list): Matrix to be multiplied
    m_b(list of list): Matrix to be multiplied

    Return:
    the matrix divided
    """
    if (m_a, m_b) is None or not (m_a, m_b) :
        raise TypeError('matrix must be a matrix (list of lists)')
    matrix_res = []
    check_float_int(m_a, "m_a ")
    check_float_int(m_b, "m_b ")
    check_lenrow(m_a, "m_a ")
    check_lenrow(m_b, "m_b ")
    check_mul(m_a, m_b)
    for row in range(len(m_a)):
        new_list = []
        for col in range(len(m_b[0])):
            sum = 0
            for step in range(len(m_b)):
                sum += m_a[row][step] * m_b[step][col]
            new_list.append(sum)
        matrix_res.append(new_list)
    print(matrix_res)

def check_float_int(matrix, name):
    """function that checks for the members of the matrix
    is not int or float"""
    if type(matrix) is not list:
        raise TypeError(name + "must be a list")
    elif not matrix:
        raise ValueError(name + "can't be empty")
    for row in matrix:
        if type(row) is not list:
            raise TypeError(name + 'must be a list of lists')
        elif not row or not matrix:
            raise ValueError(name + "can't be empty")
        for num in row:
            if type(num) in (int, float):
                continue
            else:
                raise TypeError(name + "should contain only integers or floats")

def check_lenrow(matrix, name):
    """function that check the lenghts of the rows"""
    equal = []
    for row in matrix:
        equal.append(len(row))
    if len(set(equal)) != 1 and len(equal) > 1:
        raise TypeError("Each row of the " + name + "must have the same size")

def check_mul(m_a, m_b):
    """function that checks if the two matrix can be multiplied"""
    if len(m_a[0]) is not len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
