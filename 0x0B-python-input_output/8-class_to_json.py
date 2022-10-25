#!/usr/bin/python3

"""8-class_to_json module"""


def class_to_json(obj):
    """Returns the dictionary contains all attributes of an instance"""
    return obj.__dict__
