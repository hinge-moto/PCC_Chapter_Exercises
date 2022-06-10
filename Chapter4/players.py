# April 20.2022

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:])

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

print("\nThe first three items in this list are:")
print(players[:3])

print("\nThree items from the middle of the list are:")
print(players[1:4])

print("\nThe last three items in the list are:")
print(players[-3:])
