# May 22.2022

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(f"text_files/{filename}") as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has approximately {num_words} in it.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for file in filenames:
    count_words(file)
