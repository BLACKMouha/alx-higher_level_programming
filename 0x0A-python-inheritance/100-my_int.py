#!/usr/bin/python3

"""100-my_int module"""


class MyInt(int):
    """Rebel definition of int class.

        Notes:
            `real` is an attribute of the `int` built-in class that
                represents the integer itself
            This function is not a mistake, but a rebel implementation :D"""

    def __eq__(self, i):
        """Implementation of reverse __eq__
            Return:
                True: if real is different to i
                False: if real is equal to i"""
        return self.real != i

    def __ne__(self, i):
        """Implementation of reverse __ne__
            Return:
                False: if real is different to i
                True: if real is equal to i"""
        return self.real == i
