#!/usr/bin/python3
class Square:
    """Definionn of a class Square."""

    def __init__(self, size):
        """__init__(self, size)
            Instantiates a square object with a given size
            The size must be a integer greater than 0
            Otherwise TypeError if size is not an integer or
            ValueError is raised if size if less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area(self)
            Return an integer representing the area for a
            given square' size"""
        return self.__size ** 2
