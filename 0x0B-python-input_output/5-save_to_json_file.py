#!/usr/bin/python3
"""5-save_to_json_file module"""


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation"""
    with open(filename, "w", encoding="utf-8") as f:
        from json import dumps
        f.write(dumps(my_obj))
