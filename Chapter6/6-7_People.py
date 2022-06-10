# May 14.2022

people = []

bianca = {'name': 'bianca',
          'age': 33,
          'race': 'indigenous',
          'gender': 'female',
          }
people.append(bianca)

matt = {'name': 'matt',
        'age': 33,
        'race': 'whitebread',
        'gender': 'man',
        }
people.append(matt)

dylan = {'name': 'dylan',
         'age': 34,
         'race': 'mutt',
         'gender': 'man',
         }
people.append(dylan)

for person in people:
    name = f"{person['name'].title()}"
    age = person['age']
    race = person['race']
    gender = person['gender']
    print(f"\n{name}'s Age is {age}\n\tRace is {race}"
          "\n\tGender is {gender}.")
