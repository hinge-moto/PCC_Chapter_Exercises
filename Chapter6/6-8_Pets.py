# May 14.2022

pets = []

dog = {'animal': 'dog',
       'name': 'ruff',
       'breed': 'labrador',
       'owner': 'todd',
       'age': 3,
       }
pets.append(dog)

cat = {'animal': 'cat',
       'name': 'mitzi',
       'breed': 'siamese',
       'owner': 'daniel',
       'age': 12,
       }
pets.append(cat)

parrot = {'animal': 'parrot',
          'name': 'fritz',
          'breed': 'macaw',
          'owner': 'reginald',
          'age': 46,
          }
pets.append(parrot)

rat = {'animal': 'rat',
       'name': 'sniffle',
       'breed': 'common rat',
       'owner': 'dylan',
       'age': 2
       }
pets.append(rat)

for pet in pets:
    animal = pet['animal']
    name = pet['name'].title()
    breed = pet['breed'].title()
    owner = pet['owner'].title()
    age = pet['age']
    print(f"The {animal} {name} is a {breed}, age {age} and owned by {owner}.")

for pet in pets:
    print(f"\nLet me tell you about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key.title()}: {value}")
