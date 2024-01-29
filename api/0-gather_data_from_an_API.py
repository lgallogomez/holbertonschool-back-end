#!/usr/bin/python3
"""
Python script returns employee name, number of tasks done
and list of progress
"""


import json
import requests
from sys import argv


if __name__ == "__main__":
    """getting info from todos api"""
    user_id = argv[1]
    api_todos = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    to_do_response = requests.get(api_todos)
    json_to_do = to_do_response.json()

    """getting user from users api"""
    api_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(api_url)
    j_obj = response.json()

    tasks_done = 0
    all_tasks = 0
    for item in json_to_do:
        if item["completed"] is True:
            tasks_done += 1

    for item in json_to_do:
        all_tasks += 1

    user = j_obj["name"]
    print(f"Employee {user} is done with({tasks_done}/{all_tasks}):")
    """printing  """

    for item in json_to_do:
        if item["completed"] is True:
            print(f"\tTS{item['title']}")
