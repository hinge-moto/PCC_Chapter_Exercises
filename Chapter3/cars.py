cars = ['bmw', 'toyota', 'chevy', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

print("\nHere is the oringinal list:")
butts = ['smelly', 'poopy', 'flat', 'phat', 'dimpled']
print(butts)

print("\nHere is the sorted list:")
print(sorted(butts))

print("\nHere is the original list again:")
print(butts)

print("\nHere is the list is reverse:")
print(sorted(butts, reverse=True))

butts.reverse()
print('')
print(butts)

print('')
print(len(butts))
