# May 23.2022

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(f"text_files/{filename}", 'w') as f:
    json.dump(numbers, f)
