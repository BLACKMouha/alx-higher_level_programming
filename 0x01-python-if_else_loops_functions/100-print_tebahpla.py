#!/usr/bin/python3

for c in range(65, 91):
    print('{}'.format(chr(c + 32) if c % 2 == 0 else chr(c)), end='')
