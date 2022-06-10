# May 23.2022

import json

filename = 'numbers.json'
with open(f"text_files/{filename}") as f:
    numbers = json.load(f)

print(numbers)
