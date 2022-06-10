# April 19, 2022

dead_guest = ['kimon nicolaides', 'ella fitzgerald', 'nina simone']
print(dead_guest)

print("\nHey " + dead_guest[0].title() + ", let's party.")
print("Hey " + dead_guest[1].title() + ", let's party.")
print("Hey " + dead_guest[2].title() + ", let's party.")

print("\nA larger table is available, let's goooooo!")

dead_guest.insert(0, 'bob dole')
dead_guest.insert(2, 'earthworm jim')
dead_guest.append('sister rosetta tharpe')
#print(dead_guest)

print("\nHey " + dead_guest[0].title() + ", let's party.")
print("Hey " + dead_guest[1].title() + ", let's party.")
print("Hey " + dead_guest[2].title() + ", let's party.")
print("Hey " + dead_guest[3].title() + ", let's party.")
print("Hey " + dead_guest[4].title() + ", let's party.")
print("Hey " + dead_guest[5].title() + ", let's party.")

dead_guest_length = str(len(dead_guest))
print("\nThe number of guests attending this mash is " + dead_guest_length)
