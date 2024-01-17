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

    df2 = pd.DataFrame(json_user_info)

    selected_rows_df1 = df1[["userId"]] 
    selected_rows_df1_part_2 = df1[["completed", "title"]]
    selected_rows_df2 = df2[["username"]]

    #combined_df = pd.concat([selected_rows_df1, selected_rows_df2], ignore_index=True)

    combined_df = pd.concat([selected_rows_df1["userId"], selected_rows_df2["username"], selected_rows_df1_part_2["completed"], selected_rows_df1_part_2["title"]])
    combined_df.to_csv("USER_ID")
    