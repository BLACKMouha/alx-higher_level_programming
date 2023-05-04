#!/usr/bin/python3
'''
Fetches ALX intranet status page and displays some info
'''
import requests


if (__name__ == '__main__'):
    r = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(r.text),
                                                                 r.text))
