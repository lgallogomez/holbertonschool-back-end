#!/usr/bin/python3

'''
file gathers info from api
'''

import requests
from sys import argv
import json


user_id = argv[1]

#api_url = f"https://jsonplaceholder.typicode.com/todos/{user_id}"
api_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
#print(type(user_id))

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