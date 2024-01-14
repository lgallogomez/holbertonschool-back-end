#!/usr/bin/python3

"""
module gathers data using api and displays info
"""


import requests
from sys import argv
import json

"""
module gathers data
"""
user_id = argv[1]

api_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

api_to_dos = "https://jsonplaceholder.typicode.com/todos/"

to_do_response = requests.get(api_to_dos)
json_to_do = to_do_response.json()
print(json_to_do)

list = []
for item in json_to_do:
    if item["userId"] == user_id:
        print(item)

user_id_int = int(user_id)

response = requests.get(api_url)
dicti_json = response.json()
print(response)
print(type(dicti_json))
print(dicti_json)
print(f"Employee {dicti_json['name']} is done with ")

if __name__ == "__main__":
    main()