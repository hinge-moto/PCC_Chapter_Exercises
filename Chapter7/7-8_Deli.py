# May 16.2022

sandwich_orders = ['ham', 'pb&j', 'crispy chicken', 'mayonnaise', 'dirt']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"Heck of a {sandwich.title()} sandwich you have there. Respect.")
    finished_sandwiches.append(sandwich)

print("\nThese are the sandwiches that will go to Vallhalla:")
for sandwich in finished_sandwiches:
    print(f" - {sandwich.title()}")
