#!/usr/bin/python3

"""

Write a program that imports all functions from the file
calculator_1.py and handles basic operations

- Usage: ./100-my_calculator.py a operator b
	- If the number of arguments is not 3, the program:
		- prints "Usage: ./100-my_calculator.py <a>
			<operator> <b>"
		- exit with the value 1
	- operator can be:
		- "+" for addition
		- "-" for substraction
		- "*" for multiplication
		- "/" for division
	- If the operator is not one of the above:
		- prints "Unknown operator. Avaiblable operators: +,
			-, * and /"
		- exit with value 1
	- You can cast a and b into integers with int()
	- The result should be printed like this: "<a>
		<operator> <b> = <result>
"""

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]

    if op == '+':
        print('{} {} {} = {}'.format(a, op, b, add(a, b)))
    elif op == '-':
        print('{} {} {} = {}'.format(a, op, b, sub(a,b)))
    elif op == '*':
        print('{} {} {} = {}'.format(a, op, b, mul(a, b)))
    elif op == '/':
        print('{} {} {} = {}'.format(a, op, b, div(a, b)))
    else:
        print("Unknown operator. Avaiblable operators +, -, * and /")
        exit(1)






































































