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
        """area(self)
            Return an integer representing the area for a
            given square' size"""
        return self.size ** 2

    @property
    def size(self):
        """Getting the size of the current instance"""
        return self.__size

    @size.setter
    def size(self, test):
        """Setting the size of the current instance
            Agrs:
                test (int): integer argument

            Raises:
                TypeError: if test is not type int.

            Return:
                size of the square"""
        if not isinstance(test, int):
            raise TypeError("size must be an integer")
        self.__size = test

    def my_print(self):
        """Prints '#' characters to draw a square of the given size
            If the size is 0, a new line is printed"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end="")
            print()
