#!/usr/bin/python3
"""
Fetches an url and displays info about the body
"""

import urllib.request

if (__name__ == '__main__'):
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as res:
        body = res.read()
        print('Body reponse:')
        print('    - type: {}\n    - content: {}\n    - utf8 content: {}'
              .format(type(body), body, res.msg))
