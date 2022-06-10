# May 16.2022

responses = {}

polling_active = True

while polling_active:
    user_name = input("Please enter your name: ")
    vacation = input("Where would you love to vacation: ")

    responses[user_name] = vacation
    repeat = input("\nRetake poll? y/n: ")
    if repeat == 'n':
        polling_active = False

print("\n++-- Poll results --++")
for user, vacation in responses.items():
    print(f"  {user.title()} - {vacation.title()}")
