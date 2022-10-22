#!/usr/bin/python3

"""6-base_geometry module"""


class BaseGeometry:
    """Definition of BaseGeometry class"""
    def area(self):
        """raise an Exception message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks if `value` is valid

            Raises:
                TypeError: if `value` is not an integer
                ValueErrr: if `value` <= 0"""
        if type(value) is not int:
            raise TypeError("{name} must be an integer".format(name=name))

        if value <= 0:
            raise ValueError('{name} must be greater than 0'.format(name=name))
