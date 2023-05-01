#!/usr/bin/python3
"""
Sends a POST request to the URL with the email, both passed as arguments
"""

import urllib.request
from sys import argv

if (__name__ == '__main__'):
    url = argv[1]
    data = {'email': argv[2]}
    data = urllib.parse.urlencode(data)
    data = data.encode('ascii')
    with urllib.request.urlopen(url, data) as res:
        body = res.read()
        print(body.decode('utf-8'))
