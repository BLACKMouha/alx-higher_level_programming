#!/usr/bin/python3

"""1-rectangle.py"""


class Rectangle():
    """Definition of a class Rectangle"""
    def __init__(self, width=0, height=0):
        """Initializing a Rectangle instance(object)
            Args:
                width: the width of the rectangle
                height: the height of the rectangle
            Return: Nothing"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width  Rectangle instance

            Usage: instance_name.width

            Return: the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set/Update the width of the Rectangle instance

            Usage: instance_name.width

            Raises:
                TypeError: type of value is not an integer
                ValueError: value < 0

            Return: Nothing special"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """Retrieve the height  Rectangle instance

            Usage: instance_name.height

            Return: the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set/Update the height of the Rectangle instance

            Usage: instance_name.height

            Raises:
                TypeError: type of value is not an integer
                ValueError: value < 0

            Return: Nothing special"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    def area(self):
        """Computes the area of a rectangle
            Usage: instance_name.area()

            Return: an integer, the are of a rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Computes the perimeter of a rectange
            Usage: instance_name.perimeter()

            Return: an integer, the parameter of a rectangle"""
        return (self.width + self.height) * 2
