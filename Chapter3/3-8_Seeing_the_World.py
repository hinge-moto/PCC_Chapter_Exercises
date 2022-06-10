# April 19/2022

nice_places = ['pakistan', 'india', 'china', 'russia', 'chile']

print("Here is the OG list:")
print(nice_places)

print("\nHere is the alphabetically sorted list:")
print(sorted(nice_places))

print("\nProof the list is unmodified:")
print(nice_places)

print("\nHere is the list in reverse alphabetical order:")
print(sorted(nice_places, reverse=True))

print("\nProof the list is unmodified:")
print(nice_places)

nice_places.reverse()
print("\nThe list is now permanently reversed:")
print(nice_places)

nice_places.reverse()
print("\nThe list is reversed to its' original order:")
print(nice_places)

nice_places.sort()
print("\nThe list is now permanently sorted in alphabetical order:")
print(nice_places)

nice_places.sort(reverse=True)
print("\nThe list is now permanently sorted in reverse alphabetical order:")
print(nice_places)

print("\nProof the list is in reverse alphabetical order:")
print(nice_places)
