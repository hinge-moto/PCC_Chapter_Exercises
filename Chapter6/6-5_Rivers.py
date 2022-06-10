# April 27.2022

rivers = {
    'nile': 'egypt',
    'indus': 'pakistan',
    'north saskatchewan': 'alberta',
    }
    
for river, place in rivers.items():
    print(f"The {river.title()} runs through {place.title()}.\n")

for river in rivers.keys():
    print(river.title())
    
print()
for place in rivers.values():
    print(place.title())
