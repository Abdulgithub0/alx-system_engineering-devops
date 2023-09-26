#!/usr/bin/python3

"""Gather data from an API.
    The script must display on the standard output the employee
        TODO list progress in this exact format:
    First line: Employee EMPLOYEE_NAME is done with
        tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
    EMPLOYEE_NAME: name of the employee
    NUMBER_OF_DONE_TASKS: number of completed tasks
    TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum
        of completed and non-completed tasks.
    Second and N next lines display the title of completed tasks:
        TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
"""

import requests as req
import sys


def user_progress(arg) -> None:
    """display a user details and todos list progress"""
    try:
        id_ = int(arg[1])
        # get user detail  overview
        resp = req.get(f"https://jsonplaceholder.typicode.com/users/{id_}")
        name = resp.json()['name']
        # get todos list details
        url = f"https://jsonplaceholder.typicode.com/user/{id_}/todos"
        todos = req.get(url).json()
        total_len = len(todos)
        complete = 0
        for todo in todos:
            if todo["completed"]:
                complete += 1
        print(f"Employee {name} is done with tasks({complete}/{total_len}):")
        [print("\t {}".format(t['title'])) for t in todos]
    except Exception as e:
        pass


if __name__ == "__main__":
    """launch program"""
    user_progress(sys.argv)
