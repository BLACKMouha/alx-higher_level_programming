#!/usr/bin/python3

"""8-rectangle module"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """Definition of Rectangle class based on BaseGeometry class"""

    def __init__(self, width, height):
        """Initializes a Rectangle instance
            Parameters:
                width: integer, width
                height: integer, height"""
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)

        self.__width = width
        self.__height = height
