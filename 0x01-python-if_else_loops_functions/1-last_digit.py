#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

number = str(number)
len_number = len(number)
last_digit = int(number[len_number - 1])

print('Last digit', number, 'is', last_digit, end='')
if last_digit > 5:
    print(' and is greater than 5')
if last_digit < 6 and last_digit != 0:
    print(' and is less than 6 and not 0')
