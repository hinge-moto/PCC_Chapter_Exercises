# May 21.2022

filename = 'pi_digits.txt'

with open(f'text_files/{filename}') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
