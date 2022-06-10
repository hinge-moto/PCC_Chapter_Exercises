# May 23.2022

import json

def fav_number():
    """Ask user for their favourite number."""
    filename = 'favourite_number.json'
    fav_number = input("What is your favourite number? ")
    with open(f"text_files/{filename}", 'w') as f:
        json.dump(fav_number, f)

def read_number():
    """Read the user's favourite number."""
    filename = 'favourite_number.json'
    with open(f"text_files/{filename}") as f:
        fav_number = json.load(f)
    print(f"We remember your favourite number is {fav_number}.")

fav_number()
read_number()
