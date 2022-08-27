#!/usr/bin/python3
"""

Write a function that prints a string in uppercase
followed by a new line

Prototype: def uppercase(str):
You can only use one loop in your code
You are not allowed to import any module
You are not allowed to use str.upper() and str.isupper()

"""


"""

To print a string in uppercase, each character that is
lowercase is converted and printed in uppercase. Others
characters are printed as-is.

"""
lowercase = __import__('7-islower').lowercase
def uppercase(str):
    for c in str:
    	print('{}'.format(c if lowercase(c) else chr(ord(c) - 32)), end='')
    print()





















