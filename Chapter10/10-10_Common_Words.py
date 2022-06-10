# May 23.2022

def word_count(word):
    """Count the number of instances of a word in a given text file."""
    
    filename = input("Please enter the name of the text file you would like to "
                   "analyze: ")
    with open(f"text_files/{filename}") as f:
        count = f.read().count(f' {word} ')
        return count

print(word_count('the'))
print(word_count('The'))
