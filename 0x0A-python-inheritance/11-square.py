#!/usr/bin/python3

"""10-square module"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class definition based on Rectangle"""

    def __init__(self, size):
        """Initializes a Square instance after validating the specified size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
    def area(self):
        """Computes the area of square"""
        return self.__size ** 2

    def __str__(self):
        s = "[" + str(self.__class__.__name__) + "] "
        s += str(self.__width) + "/" + str(self.__height)
        return s
