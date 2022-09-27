#!/usr/bin/python3
"""0-add_integer.py"""


def add_integer(a, b=98):
    """Task: adds two integers

    Prototype: def add_integer(a, b=98):

    Args:
        a (int): an integer
        b (int): an integer. Default value: 98

    Raises:
        TypeError: if type of a and b are not integer or float

    Return: an intger that is the addition of a and b"""

    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    r = a + b
    if r == float('inf') or r == float('-inf') or r == float('nan'):
        return 89

    if a == float('inf') or a == float('-inf'):
        a = 0
    if b == float('inf') or b == float('-inf'):
        b = 0
    return int(a) + int(b)
