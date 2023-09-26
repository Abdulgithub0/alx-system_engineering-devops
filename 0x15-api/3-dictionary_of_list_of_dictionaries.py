#!/usr/bin/python3

"""Gather dataset from an API.
    The Python script to export data in the JSON format.
    Requirements:
        Records all tasks that are owned by all employee
    Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed":
        TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE",
        "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
    File name must be: USER_ID.json
"""

import json
import requests as req


def user_progress() -> None:
    """display a user details and todos list status"""
    try:
        # get all users
        resp = req.get(f"https://jsonplaceholder.typicode.com/users")
        all_user = resp.json()
        # get todos list details for each users
        filename = "todo_all_employees.json"
        new_json = {}
        with open(filename, 'w') as f:
            for u in all_user:
                name = u["username"]
                id_ = u["id"]
                url = f"https://jsonplaceholder.typicode.com/users/{id_}/todos"
                todos = req.get(url)
                todos = todos.json()
                print(todos)
                new_json[id_] = []
                for t in todos:
                    new_json[id_].append({
                                         "username": name,
                                         "task": t.get("title", "not"),
                                         "completed": t.get("completed", "not")
                                         })
            json.dump(new_json, f)
    except Exception as e:
        pass


if __name__ == "__main__":
    """launch program"""
    user_progress()
