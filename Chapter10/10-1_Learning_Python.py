# May 22.2022

filename = 'learning_python.txt'

with open(f'text_files/{filename}') as file_object:
    contents = file_object.read()
print(contents.replace('Python', 'Rust'))

with open(f'text_files/{filename}') as file_object:
    for line in file_object:
        print(line.strip())

with open(f'text_files/{filename}') as file_object:
    lines = file_object.readlines()

print()
for line in lines:
    print(line.strip())
