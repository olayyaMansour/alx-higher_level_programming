#!/usr/bin/python3
"""
A Python script that takes your GitHub credentials (username and password/token)
and uses the GitHub API to display your id.
Uses Basic Authentication with a personal access token as the password.
Uses the requests package.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, password))

    try:
        user_info = response.json()
        print(user_info['id'])
    except ValueError:
        print(None)
