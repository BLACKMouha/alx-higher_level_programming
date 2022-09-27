#!/usr/bin/python3
"""5-text_indentation.py"""


def text_indentation(text):
    """Task: write a function that prints a text with two lines after each of
        this character '.', ',', '?', ':'

        Prototype: def text_indentation(text):

        Args: text (string): a string

        Raises:
            TypeError: if text is not a string

        Return:
            Nothing special"""

    if type(text) != str:
        raise TypeError('text must be a string')
    r_text = text[::-1]
    i = len(r_text) - 1
    while i - 1 >= 0:
        if r_text[i] == ' ':
            if 65 <= ord(r_text[i-1]) <= 90 or 97 <= ord(r_text[i-1]) <= 122\
                    or r_text[i-1] == ' ':
                pass

        if r_text[i] in ['.', '?', ':']:
            print(r_text[i], end='\n\n')
            if r_text[i-1] == ' ':
                i -= 1
        else:
            print(r_text[i], end='')
        i -= 1

    if r_text[i] != ' ':
        print(r_text[i], end='')
