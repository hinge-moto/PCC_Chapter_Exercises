# April 27.2022

favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
    
for name, language in favourite_languages.items():
    print(f"{name.title()}'s favourite language is {language}.")

print()

gotta_poll = ['jen', 'robert', 'damien', 'edward', 'roger']
for name in gotta_poll:
    if name in favourite_languages.keys():
        print(f"Thank you {name.title()} for taking the poll.")
    else:
        print(f"Take the poll {name.title()}!")
