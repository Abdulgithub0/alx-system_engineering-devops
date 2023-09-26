#!/usr/bin/python3

"""Gather dataset from an API.
    The Python script to export data in the CSV format.
    Requirements:
        Records all tasks that are owned by this employee
        Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS",
        "TASK_TITLE" File name must be: USER_ID.csv
"""

import csv
import requests as req
import sys


def user_progress(arg) -> None:
    """display a user details and todos list status"""
    try:
        id_ = int(arg[1])
        # get user detail overview
        resp = req.get(f"https://jsonplaceholder.typicode.com/users/{id_}")
        details = resp.json()
        user = details['username']
        # get todos list details
        url = f"https://jsonplaceholder.typicode.com/user/{id_}/todos"
        todos = req.get(url).json()
        filename = f"{id_}.csv"
        with open(filename, 'w', newline='') as f:
            write = csv.writer(f, quoting=csv.QUOTE_ALL)
            for todo in todos:
                write.writerow([id_, user, todo['completed'], todo['title']])
    except Exception as e:
        pass


if __name__ == "__main__":
    """launch program"""
    user_progress(sys.argv)
