#!/usr/bin/python3

"""3-is_kind_of_class module"""


def is_kind_of_class(obj, a_class):
    """Checks if `obj` is an instance of `a_class`

        Return:
            True: if `obj` is an instance of a_class
            False: Otherwise"""

    return isinstance(obj,  a_class)
