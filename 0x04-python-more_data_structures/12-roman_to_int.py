#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) is not str:
        return 0

    roman_numbers =\
        {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    idx = len(roman_string) - 1
    r = roman_numbers[roman_string[idx]]
    for i in range(idx - 1, -1, -1):
        if roman_numbers[roman_string[i]] >= roman_numbers[roman_string[i+1]]:
            r += roman_numbers[roman_string[i]]
        else:
            r -= roman_numbers[roman_string[i]]
    return r
