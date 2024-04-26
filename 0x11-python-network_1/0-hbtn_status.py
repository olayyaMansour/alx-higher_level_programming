#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request

def fetch_status(url):
    """
    Fetches the status from the given URL and returns response details.
    
    Args:
        url (str): The URL to fetch status from.
    
    Returns:
        dict: Dictionary containing response details.
    """
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        html = response.read()
        return {
            "type": type(html),
            "content": html,
            "utf8_content": html.decode('utf-8')
        }

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response_details = fetch_status(url)
    
    print("Body response:")
    for key, value in response_details.items():
        print(f"\t- {key}: {value}")

