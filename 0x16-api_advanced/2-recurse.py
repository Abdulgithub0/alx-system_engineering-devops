#!/usr/bin/python3
"""a recursive function that queries the Reddit
API and returns a list containing the titles of
all hot articles for a given subreddit. If no results are
found for the given subreddit, the function should return None.
"""

import requests


def recurse(subreddit, hot_list=[],
            args={"after": None, "count": 0, "limit": 100}):
    """return a list of subreddit hot articles"""
    url = f"https://reddit.com/r/{subreddit}/hot/.json"
    head = {"User-Agent": "Student.Alx.task:v1.0.0"}
    resp = requests.get(url, headers=head, params=args)
    if resp.status_code == 200:
        try:
            parent_data = resp.json()["data"]
            children_data = parent_data["children"]
            args["after"] = parent_data["after"]
            args["count"] += parent_data["dist"]
            for data in children_data:
                hot_list.append(data.get("data").get("title"))
        except Exception as e:
            pass
    if args.get("after"):
        recurse(subreddit, hot_list, args)
    r = hot_list if len(hot_list) != 0 else None
    return r
