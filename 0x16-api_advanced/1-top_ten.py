#!/usr/bin/python3
""" a function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """print out titles"""
    url = f"https://reddit.com/r/{subreddit}/hot/.json"
    head = {"User-Agent": "Student.Alx.task:v1.0.0"}
    resp = requests.get(url, headers=head, params={"limit": 10})
    if resp.status_code == 200:
        try:
            children = resp.json().get("data").get("children")
            for data in children:
                print(data.get("data").get("title"))
        except Exception as e:
            pass
    print(None)
