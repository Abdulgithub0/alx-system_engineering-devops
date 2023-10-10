#!/usr/bin/python3
"""a recursive function that queries the Reddit API,
parses the title of all hot articles, and prints
a sorted count of given keywords
(case-insensitive, delimited by spaces. Javascript should
count as javascript, but java should not).
"""

import requests


def count_words(subreddit, word_list=[], hot_list=[],
                args={"after": None, "count": 0, "limit": 100}):
    """print a sorted of list of find keyword in
    title of subreddit hot articles
    """
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
                hot_list.append(data.get("data").get("title").lower())
        except Exception as e:
            pass
    if args.get("after"):
        count_words(subreddit, word_list, hot_list, args)
    else:
        if (word_list and hot_list):
            word = [w.lower().split() for w in word_list]
            lst = sorted([x for w in word for x in w])
            dic = {}
            for kw in lst:
                dic[kw] = 0
                for word in hot_list:
                    dic[kw] += word.split().count(kw)
        [print(k + ':', v) for k, v in dic.items() if v != 0]
