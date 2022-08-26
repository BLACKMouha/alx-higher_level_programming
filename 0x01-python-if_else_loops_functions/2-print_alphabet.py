#!/usr/bin/python3

"""
Write a function that prints the ASCII alphabet, not
followed by a new line

- You can only use 1 print() funtion with string format
- You can only use one loop in your code
- You are not allowed to store characters in a variable
- You are not allowed to import any module
"""

for ascii_code in range(97, 123):
    print("{:s}".format(chr(ascii_code)), end='')
