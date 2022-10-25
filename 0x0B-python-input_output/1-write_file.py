#!usr/bin/python3

"""1-write_file module"""


def write_file(filename="", text=""):
    """Write `text` in `filename`"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
