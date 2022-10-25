#!/usr/bin/python3

"""6-load_from_json_file module"""


def load_from_json_file(filename):
    """Given a JSON file, loads the JSON representation into a Python Object"""
    with open(filename, mode="r", encoding="utf-8") as f:
        from json import loads
        return loads(f.read())
