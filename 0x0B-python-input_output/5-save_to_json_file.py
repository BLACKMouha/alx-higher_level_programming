#!/usr/bin/python3
"""5-save_to_json_file module"""

from json import dumps


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation"""

    write_file = __import__('1-write_file').write_file

    write_file(filename, dumps(my_obj))
