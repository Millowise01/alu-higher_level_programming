#!/usr/bin/python3

'''
this module contains a function that multiplies 2 matrices
'''
def matrix_mul(m_a, m_b):
    """Multiplies 2 matrices
    Args:
        m_a (list): matrix a
        m_b (list): matrix b
    Returns:
        list: new matrix
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
        if len(row) != len(m_a[0]):
            raise TypeError("m_a must be a list of lists")
        for item in row:
            if type(item) is not int and type(item) is not float:
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")
        if len(row) != len(m_b[0]):
            raise TypeError("m_b must be a list of lists")
        for item in row:
            if type(item) is not int and type(item) is not float:
                raise TypeError("m_b should contain only integers or floats")
    if len(m_a) is 0 or len(m_a[0]) is 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) is 0 or len(m_b[0]) is 0:
        raise ValueError("m_b can't be empty")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    return [[sum(a * b for a, b in zip(m_a_row, m_b_col)) for m_b_col in zip(*m_b)] for m_a_row in m_a]

print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
