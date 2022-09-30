#!/usr/bin/python3
"""100-matrix_mul module"""

def matrix_mul(m_a, m_b):
    """matrix_mul computes the multiplication of two matrix. A matrix in Python
        is a list of lists. In this case, it's a list of lists of integers

        Prototype: def matrix_mul(m_a, m_b):

        Args:
            m_a: matrix
            m_b: matrix
        Raises
            TypeError:

                if are not list
                if lists of lists
                if list of lists of integers or floats
                if the size of a rows are of a matrix are different

            ValueError:
                if arguments are empty
                if the number of columns in the first matrix is different to
                    the number of rows in the second matrix

        Return:
            a new matrix with the same number of rows of the first matrix and
                the same number of colums of the second matrix"""
    if type(m_a) != list:
        raise TypeError('m_a must be a list')

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")

    for ls in m_a:
        if type(ls) != list:
            raise TypeError('m_a must be a list of lists')
        len_ls = len(m_a[0])
        if len(ls) != len_ls:
            raise TypeError('each row of m_a must be of the same size')
        for i in ls:
            if type(i) != int and type(i) != float:
                raise TypeError('m_a should contain only integers or floats')

    if type(m_b) != list:
        raise TypeError('m_b must be a list')

    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for ls in m_b:
        if type(ls) != list:
            raise TypeError('m_b must be a list of lists')
        len_ls = len(m_b[0])
        if len(ls) != len_ls:
            raise TypeError('each row of m_b must be of the same size')
        for i in ls:
            if type(i) != int and type(i) != float:
                raise TypeError('m_b should contain only integers or floats')

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    m_r = []
    r = 0
    for i in range(0, len(m_a)):
        sublist = []
        for j in range(0, len(m_b[i])):
            r = 0
            for k in range(0, len(m_b)):
                r += m_a[i][k] * m_b[k][j]
            sublist.append(r)
        m_r.append(sublist)

    return m_r
