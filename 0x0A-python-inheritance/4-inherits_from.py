#!/usr/bin/python3

"""4-inherits_from module"""


def inherits_from(obj, a_class):
    """Checks if `obj` is an instance of a class that inherited from the
        `a_class`

        Return:
            True: if `obj` is an instance of a class that inherited from
                `a_class`
            False: Otherwise"""

    return (type(obj) is not a_class) and isinstance(obj, a_class)
