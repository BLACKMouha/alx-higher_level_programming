#!/usr/bin/python3
"""
Fetches an url and displays info about the body
"""

import urllib.request

if (__name__ == '__main__'):
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as res:
        body = res.read()
        print('Body response:')
        print('\t- type: {}\n\t- content: {}\n\t- utf8 content: {}'
              .format(type(body), body, body.decode('utf-8')))
