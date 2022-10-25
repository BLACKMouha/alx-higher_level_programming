#!/usr/bin/python3

"""10-student module"""


class Student:
    """Implementation of Student class"""

    def __init__(self, first_name, last_name, age):
        """Initializes an instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary description of an instance"""
        new_dict = dict()

        if attrs is not None:
            for attr, value in self.__dict__.items():
                if attr in attrs:
                    new_dict[attr] = value
            return new_dict
        else:
            return self.__dict__
