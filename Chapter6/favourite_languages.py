# April 24.2022

favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
    
language = favourite_languages['sarah'].title()
print(f"Sarah's favourite language is {language}.\n")

# Using dictionary looping with .items():
for name, language in favourite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}.")
    
# Using the .keys() method:
print()
for name in favourite_languages.keys():
    print(name.title())


# Complex loop doing all the things:
print()
friends = ['phil', 'sarah']
for name in favourite_languages.keys():
    print(name.title())
    
    if name in friends:
        language = favourite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")


# Checking for a name in dictionary:
print()
if 'erin' not in favourite_languages.keys():
    print("Erin, please take our poll!")


# Place keys in order:
print()
for name in sorted(favourite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")


# Looping through values:
print("\nThe following languages have been mentioned:")
for language in set(favourite_languages.values()):
    print(language.title())
