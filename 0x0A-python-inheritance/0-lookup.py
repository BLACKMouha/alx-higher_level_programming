#!/usr/bin/python3

"""0-lookup module"""


def lookup(obj):
    """Prints the list of available attributes and methods of an object"""
    if isinstance(obj, object):
        return dir(obj)
