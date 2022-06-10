# April 20.2022

pizzas = ['pepperoni', 'canadian', 'meatza', 'loaded', 'cheese']
for pizza in pizzas:
    print("Gimme a slice of that " + pizza + " pizza homie.")

print("\nPizza or death!\n")

friend_pizzas = pizzas[:]
friend_pizzas.append('donair')
pizzas.append('hawaiian')

for pizza in pizzas:
    print("This is my favourite pizza on the citadel: " + pizza + ".")

print() # there has to be a better way to do this...

for pizza in friend_pizzas:
    print("My friend likes this " + pizza + " pizza a lot!")

print()
print("My pizzas:")
print(pizzas)
print("\nMy friend's pizzas:")
print(friend_pizzas)
