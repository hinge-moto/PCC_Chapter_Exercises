# May 22.2022

filename = 'guest.txt'

with open(f'text_files/{filename}', 'w') as file_object:
    user_name = input('User, what is your name: ')
    file_object.write(user_name)
