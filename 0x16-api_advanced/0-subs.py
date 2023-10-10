#!/usr/bin/python3
"""a function that queries the Reddit API
    and returns the number of subscribers 
    (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function should return 0.
"""

import requests


def number_of_subscribers(subreddit):
    """return the number of total subscribers"""
    url = f"https://reddit.com/r/{subreddit}/about/.json"
    header= {"User-Agent": "Student.Alx.task:v1.0.0"}
    resp = requests.get(url, headers=header)
    if resp.status_code == 200:
        try:
            return resp.json()["data"]["subscribers"]
        except Exception as e:
            pass
    return 0
