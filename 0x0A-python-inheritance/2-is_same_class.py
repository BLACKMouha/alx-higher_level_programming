#!/usr/bin/python3

"""2-is_same_class module"""


def is_same_class(obj, a_class):
    """Checks if `obj` is exactly an instance of `a_class`
        Return:
            True: if obj is instance of a_class
            False: Otherwise"""

    return type(obj) == a_class
