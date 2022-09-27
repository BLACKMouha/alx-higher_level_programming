#!/usr/bin/python3

"""4-print_square.py"""

def print_square(size):
    """Task: write a function that prints a square with the character '#'
        Prototype: def print_square(size):
        Args:
            size (int): the size length of the square
        Raises:
            TypeError:
                If size is not an intenger
                If size is a float and less than 0
            ValueError: If size is less than 0

        Return:
            Nothing special"""
    if type(size) != int:
        raise TypeError('size must be an integer')
    if type(size) == float and size < 0:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
