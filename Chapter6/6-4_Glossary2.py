# April 27.2022

glossary = {
    'tuple': 'immutable list',
    'range()': 'creates a range of numbers',
    'if-elif-else': 'loops according to rules',
    'dictionary': 'stores information in keys',
    'string': 'human readable text',
    'set': 'list with no duplicates',
    'IDE': 'integrated development environment',
    'python': '<3',
    }
            
print(f"- A Tuple is an {glossary['tuple']}.")
print(f"- The Range function {glossary['range()']}.")
print(f"- An if-elif-else statement {glossary['if-elif-else']}.")
print(f"- A Dictionary {glossary['dictionary']}.")
print(f"- A String contains {glossary['string']}.")

# And now using loops:
print()
for key, value in glossary.items():
    if key == 'IDE':
        print(f"IDE:\n\t {value.capitalize()}.\n")
    else:
        print(f"{key.title()}:\n\t {value.capitalize()}.\n")
        # This was tricky as hell! .title() capitalizes I in IDE
        # but then lowers every character afterwards. So IDE to Ide.
        # Could arguable do something similar for if-elif-else.
