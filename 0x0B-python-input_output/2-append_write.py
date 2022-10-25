#!/usr/bin/python3

"""1-write_file module"""


def append_write(filename="", text=""):
    """Write `text` in `filename`
        Return: the number of characters written"""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
