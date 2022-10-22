#!/usr/bin/python3

"""10-square module"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class definition based on Rectangle"""

    def __init__(self, size):
        """Initializes a Square instance after validating the specified size"""
        Rectangle.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
