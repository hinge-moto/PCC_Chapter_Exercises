# May 23.2022

import json

filename = 'username.json'

with open(f"text_files/{filename}") as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")
