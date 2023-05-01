#!/usr/bin/python3
"""
Sends a POST request to the URL with the email, both passed as arguments
"""

import urllib.request
from sys import argv

if (__name__ == '__main__'):
    url = argv[1]
    email = argv[2]
    value = {'email': email}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as res:
        body = res.read()
        print(body.decode('utf-8'))
