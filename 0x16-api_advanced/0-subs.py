#!/usr/bin/python3
"""This is 0-subs module
"""
import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API
    and returns the number of subscribers
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers={}, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
