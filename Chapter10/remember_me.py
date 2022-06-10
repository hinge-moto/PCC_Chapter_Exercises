# May 23.2022

import json

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        user_ask = input(f"Are you {username}? (y/n) ")
        if user_ask == 'y':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")
        

def get_stored_username():
    """Get stored username is available."""
    filename = 'username.json'
    try:
        with open(f"text_files/{filename}") as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(f"text_files/{filename}", 'w') as f:
        json.dump(username, f)
    return username


greet_user()
