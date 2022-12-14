#!/usr/bin/python3
"""3-say_my_name.py"""


def say_my_name(first_name, last_name=""):
    """Task: write a function that print 'My name is <first name> <last name>'.
        Prototype: def say_name(first_name, last_name=""):

        Args:
            first_name (str): string
            last_name (str): string. Default value is "" (empty string)

        Raises:
            TypeError: if first_name or last_name are not string

        Return:
            Nothing special"""
    if type(first_name) != str:
        raise TypeError('first_name must be a string')
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")

    print(f'My name is {first_name} {last_name}')
