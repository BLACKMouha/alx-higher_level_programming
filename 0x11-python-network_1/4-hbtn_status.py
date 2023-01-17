#!/usr/bin/python3
"""4-hbtn_status module
    This script fetches an URL and displays info about response
"""

if __name__ == '__main__':
    import requests

    url = 'https://alx-intranet.hbtn.io/status'
    res = requests.get(url)
    print('Body response:')
    print('\t- type: {}'.format(type(res.text)))
    print('\t- content: {}'.format(res.text))
