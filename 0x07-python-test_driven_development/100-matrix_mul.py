#!/usr/bin/python3

def matrix_mul(m_a, m_b):

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
