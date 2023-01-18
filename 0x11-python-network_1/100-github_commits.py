#!/usr/bin/python3
"""100-github_commits module
"""


if __name__ == '__main__':
    from sys import argv
    from requests import get

    owner = argv[1]
    repo = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    res = get(url, headers={"Accept": "application/vnd.github+json"})
    commits = res.json()

    while commits[i]:
        if i == 10:
            break
        print('{}: {}'.format(
            commits[i]['sha'], commits[i]['commit']['author']['name']))
