#!/usr/bin/python3

"""4-from_json_string module"""

from json import loads


def from_json_string(my_str):
    """Deserialization of JSON Representation"""
    return loads(my_str)
