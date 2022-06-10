# May 14.2022

favourite_places = {
    'jack': ['panama', 'paris', 'alberta'],
    'maria': ['toledo', 'benson', 'baton rouge'],
    'billy': ['the mall', 'home', 'calgary'],
    }

for name, places in favourite_places.items():
    print(f"\n{name.title()}'s favourite places are:")
    for place in places:
        print(f"\t{place.title()}")
