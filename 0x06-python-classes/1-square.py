#!/usr/bin/python3
"""Square class for representation of a real word square"""
    

class Square:
    """Define a class Square."""

    def __init__(self, size):
        """Called automaticcaly and immediately when instantiating a square
            object with a given size

            Args:
                size (int): size of the square.

            Raises:
                TypeError: size if not type int.
                ValueError: if size < 0.
        """
        self.__size = size
