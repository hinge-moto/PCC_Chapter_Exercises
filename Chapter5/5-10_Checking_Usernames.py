# April 24.2022

current_users = ['HOGARTH', 'ms jane', 'Dylan', 'fred', 'Neptune']
new_users = ['dylan', 'hank', 'Whiffle', 'DOG', 'Benjamin', 'FRed']

current_users_lower = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users_lower:
        print("That name is in use " + user + ", please choose another.")
    else:
        print("That name is available " + user + ".")


# start using LIST COMPREHENSION more often. Like, always.
