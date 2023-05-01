#!/usr/bin/python3
import urllib.request
"""
Fetches an url and displays info about the body
"""


if (__name__ == '__main__'):
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as res:
        body = res.read()
        print('Body reponse:')
        print('\t-type: {}\n\t-content: {}\n\t-utf 8 content: {}'
              .format(type(body), body, res.msg))
