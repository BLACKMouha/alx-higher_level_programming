#!/usr/bin/python3
class Square:
    """Definionn of a class Square."""

    def __init__(self, size=0, position=(0, 0)):
        """__init__(self, size)
            Instantiates a square object with a given size.
            The size must be a integer greater than 0. Otherwise TypeError if
            size is not an integer or ValueError is raised if size if less than
            0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if (not isinstance(position, tuple)
                or not isinstance(position[0], int)
                or not isinstance(position[1], int)
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
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)
                or len(position) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.position = value

    def area(self):
        """area(self)
            Return an integer representing the area for a
            given square' size"""
        return self.size ** 2

    def my_print(self):
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(' ', end='')
            for k in range(self.__position[1]):
                pass
            for m in range(self.__size):
                print('#', end='')
            print()
