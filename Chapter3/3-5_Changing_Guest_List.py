# April 19, 2022

dead_guest = ['kimon nicolaides', 'ella fitzgerald', 'nina simone']
#print(dead_guest)

print("\nHey " + dead_guest[0].title() + ", let's party.")
print("Hey " + dead_guest[1].title() + ", let's party.")
print("Hey " + dead_guest[2].title() + ", let's party.")

popped_guest = dead_guest.pop(2)
print("\nDue to unforseen death, " + popped_guest.title() + " cannot RSVP.")
#print(dead_guest)

dead_guest.append('john prine')
#print(dead_guest)
print("\nHey " + dead_guest[0].title() + ", let's party.")
print("Hey " + dead_guest[1].title() + ", let's party.")
print("Hey " + dead_guest[2].title() + ", let's party.")
