#!/usr/bin/python3
"""8-json_api module
    This script takes in a letter and sends a POST request to URL with the
    letter as a parameter.
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    letter = "" if len(argv) != 2 or len(argv[1]) != 1 else argv[1]
    url = 'http://0.0.0.0:5000/search_user'
    try:
        res = requests.post(url, data={'q': letter})
        json = res.json()
        if not json:
            print('No result')
        if 'id' in json and 'name' in json:
            print("[{}] {}".format(json.get('id'), json.get('name')))
    except Exception:
        print('Not a valid JSON')
