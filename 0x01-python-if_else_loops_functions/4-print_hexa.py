#!/usr/bin/python3
"""
Write a program that prints all numbers from 0 to 98
an in hexadecimal
"""
for i in range(99):
    print('{int_value} = {hex_value}'.format(int_value=i, hex_value=hex(i)))
