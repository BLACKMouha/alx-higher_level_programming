#!/usr/bin/python3
"""Square class for representation of a real word square"""


class Square:
    """Define the class Square."""

    def __init__(self, size=0, position=(0, 0)):
        """Called automaticcaly and immediately when instantiating a square
            object with a given size

            Args:
                size (int): size of the square.

            Raises:
                TypeError:
                    if size is not type int.
                    if position is not type tuple
                ValueError: if size < 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if (not isinstance(position, tuple)
                or (not isinstance(position[0], int)
                and not isinstance(position[1], int))
                or len(position) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        """size(self)
            Return the size of a square size is a property of the private
            attribute size"""
        return self.__size

    @size.setter
    def size(self, test):
        """size(self)
            A function that sets and returns the size
            attribute"""
        if not isinstance(test, int):
            raise TypeError("size must be an integer")
        if test < 0:
            raise ValueError("size must be >= 0")
        self.__size = test

    @property
    def position(self):
        """Getting the size of the current instance"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setting the size of the current instance
            Agrs:
                test (int): integer argument

            Raises:
                TypeError: if test is not type int.

            Return:
                size of the square"""
        if (not isinstance(position, tuple)
                or (not isinstance(position[0], int)
                and not isinstance(position[1], int))
                or len(position) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.position = value

    def area(self):
        """Computes the area of a square thanks to its size

            Return:
                int: an integer representing the area for a given square's
                size"""
        return self.size ** 2

    def my_print(self):
        """Prints spaces (position[1] times) then '#' (size times) characters
            to draw a square of the given size.
            If the size is 0, a new line is printed
            If position[1] is 0, no space is printed"""
        if self.__size == 0:
            print()
            return
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(' ', end='')
                for m in range(self.__size):
                    print('#', end='')
                print()
