#!/usr/bin/python3
'''
Fetches a URL, handles error if any
'''
import urllib.request
import urllib.error
from sys import argv

if (__name__ == '__main__'):
    url = argv[1]
    try:
        with urllib.request.urlopen(url) as res:
            body = res.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
