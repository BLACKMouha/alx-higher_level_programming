#!/usr/bin/python3

"""9-rectangle module"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """Definition of Rectangle class based on BaseGeometry class"""

    def __init__(self, width, height):
        """Initializes a Rectangle instance
            Parameters:
                width: integer, width
                height: integer, height"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Computes the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        s = "[Rectangle] "
        s += str(self.__width) + "/" + str(self.__height)
        return s
