#!/usr/bin/python3

"""9-student module"""


class Student:
    """Implementation of Student class"""

    def __init__(self, first_name, last_name, age):
        """Initializes an instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the dictionary description of an instance"""
        return self.__dict__
