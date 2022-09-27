#!/usr/bin/python3
"""2-matrix_divided.py"""


def matrix_divided(matrix, div):
    """Tasks: Write a function that divides all elements of a matrix.

        Prototype: def matrix_divided(matrix, div):

        Args:
            matrix: a 2D of numbers(integers or floats).
            div: an number(integer or float) dividing each atomic element
        Raise:
            TypeError:
                If matrix is not a list of lists of numbers.
                If a list inside matrix is not a list of numbers(int, float).
                If a list inside matrix has not the same length of another one.
                If div is neither an integer nor a float.

            ZeroDivisionError: if div is 0

        Return:
            a new matrix resulting to the division by div for each element of a
            sublist of matrix"""

    if not isinstance(matrix, list):
        raise TypeError('matrix must be a matrix (list of lists) of integers/\
floats')

    for i in range(len(matrix) - 1, -1, -1):
        if not isinstance(matrix[i], list):
            raise TypeError('matrix must be a matrix (list of lists) of \
integers/floats')
            break

        for el in matrix[i]:
            if not isinstance(el, float) and not isinstance(el, int):
                raise TypeError('matrix must be a matrix (list of lists) of \
integers/floats')
                break
        # endfor
        if isinstance(matrix[i], list) and isinstance(matrix[i-1], list):
            if len(matrix[i]) != len(matrix[i-1]):
                raise TypeError('matrix must be a matrix (list of lists) of \
integers/floats')
            else:
                for i, j in zip(matrix[i], matrix[i-1]):
                    if (not isinstance(i, float) and not isinstance(i, int))\
                            or (not isinstance(j, float) and
                                not isinstance(j, int)):
                        raise TypeError('matrix must be a matrix (list of \
lists) of integers/floats')
                # endfor

        if i == 0:  # if i = 0 so i - 1 = -1, OutOfRange raises
            break
    # endfor

    if type(div) != int and type(div) != float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    return list(map(lambda arr: list(map(lambda x: round((x / div), 2), arr)),
                matrix))
