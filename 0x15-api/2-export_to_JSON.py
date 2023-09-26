#!/usr/bin/python3

"""Gather dataset from an API.
    The Python script to export data in the JSON format.
    Requirements:
        Records all tasks that are owned by this employee
    Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed":
        TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE",
        "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
    File name must be: USER_ID.json
"""

import csv
import json
import requests as req
import sys


def user_progress(arg) -> None:
    """display a user details and todos list status"""
    try:
        id_ = int(arg[1])
        # get user detail overview
        resp = req.get(f"https://jsonplaceholder.typicode.com/users/{id_}")
        name = resp.json()["username"]
        # get todos list details
        url = f"https://jsonplaceholder.typicode.com/user/{id_}/todos"
        todos = req.get(url).json()
        filename = f"{id_}.json"
        id_ = str(id_)
        new_json = {id_: []}
        with open(filename, 'w', newline='') as f:
            for d in todos:
                new_json[id_].append({
                                     "username": name,
                                     "task": d["title"],
                                     "completed": d["completed"]
                                     })
            json.dump(new_json, f)
    except Exception as e:
        pass


if __name__ == "__main__":
    """launch program"""
    user_progress(sys.argv)
