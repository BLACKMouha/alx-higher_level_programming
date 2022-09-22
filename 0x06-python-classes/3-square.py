#!/usr/bin/python3
"""Square class for representation of a real word square"""


class Square:
    """Define the class Square."""

    def __init__(self, size=0):
        """Called automaticcaly and immediately when instantiating a square
            object with a given size

            Args:
                size (int): size of the square.

            Raises:
                TypeError: size if not type int.
                ValueError: if size < 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Computes the area of a square thanks to its size

            Return:
                int: an integer representing the area for a given square's
                size"""
        return self.__size ** 2
