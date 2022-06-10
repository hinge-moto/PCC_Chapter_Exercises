# May 22.2022

print('Press \'q\' to quit')

filename = 'programming_poll.txt'

while True:
    poll_response = input('TELL ME WHY YOU LIKE PROGRAMMING: ')
    if poll_response == 'q':
        break
    else:
        with open(f'text_files/{filename}', 'a') as f:
            f.write(f'{poll_response}\n')
