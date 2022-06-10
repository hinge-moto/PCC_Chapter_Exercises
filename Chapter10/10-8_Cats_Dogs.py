# May 23.2022

files = ['cats.txt', 'dogs.txt']

for file in files:
    try:
        with open(f"text_files/{file}") as pet_file:
            print(pet_file.read())
    except FileNotFoundError:
        print(f'"{file}" was not found. Please fix your shit.\n')
