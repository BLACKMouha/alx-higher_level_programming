#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# convert integer to number
number_str = str(number)
# if number was positive, retrieve directly the last digit
if number >= 0:
    last_digit = int(number_str[len(number_str) - 1])
# if number was negative, retrieve the last digit with a negative sign
if number < 0:
    last_digit = -1 * int(number_str[len(number_str) - 1])

print('Last digit of', number, 'is', last_digit, end=" ")
# if last digit is greater than 5, then print the prints the correct message
if last_digit > 5:
    print('and is greater than 5')

# if last digit is 0, then prints the correct message
if last_digit == 0:
    print('and is 0')

# if last digit is less than 6 and is not 0, then print the correct message
if last_digit < 6 and last_digit != 0:
    print('and is less than 6 and not 0')
