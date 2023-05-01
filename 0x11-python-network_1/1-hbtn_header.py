#!/usr/bin/python3
"""
Fetches an URL passed as argument and displays the value of X-Request-Id header
"""

import urllib.request
from sys import argv

if (__name__ == '__main__'):
    req = argv[1]
    with urllib.request.urlopen(req) as res:
        print(res.getheader('X-Request-Id'))
