# May 22.2022

##filename = 'guest_book.txt'
##
##with open(f'text_files/{filename}', 'a') as file_object:
##    user_name = input('User, what is your name (press \'q\' to quit): ')
##    while user_name != 'q':
##        user_name = input('User, what is your name (press \'q\' to quit): ')
##        if user_name != 'q':
##            file_object.write(f'{user_name}\n')
##        else:
##            break




# Teacher's code is vastly superior. Opens the fill inside the while-loop
#  and avoids the issue of user inputing 'q' first and tainting the file.

##filename = 'guest_book.txt'
##
##print("Enter 'quit' when you are finished.")
##while True:
##    name = input("\nWhat's your name? ")
##    if name == 'quit':
##        break
##    else:
##        with open(filename, 'a') as f:
##            f.write(f"{name}\n")
##        print(f"Hi {name}, you've been added to the guest book.")




filename = 'guest_book.txt'

print('Press \'q\' to quit')
while True:
    user_name = input('User, what is your name: ')
    if user_name == 'q':
        break
    else:
        with open(f'text_files/{filename}', 'a') as f:
            f.write(f'{user_name}\n')
