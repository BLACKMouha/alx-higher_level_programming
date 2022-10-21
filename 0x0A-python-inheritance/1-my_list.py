#!/usr/bin/python3

"""1-my_list module"""


class MyList(list):
    """MyList is a subclass of list"""

    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
