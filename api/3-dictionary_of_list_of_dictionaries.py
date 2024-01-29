#!/usr/bin/python3
"""
exporting json file taken from api, into a csv file
"""

import json
import pandas as pd
import requests
from sys import argv

if __name__ == "__main__":
    """gets info from api, then exports json file into csv"""
    user_id = argv[1]
    api_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    response = requests.get(api_url)
    json_to_dos = response.json()

    df1 = pd.DataFrame(json_to_dos)

    """getting user from users api"""
    api_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(api_url)
    json_user_info = response.json()