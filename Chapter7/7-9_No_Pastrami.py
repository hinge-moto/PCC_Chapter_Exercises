# May 16.2022

sandwich_orders = ['pastrami', 'pb&j', 'pastrami', 'mayonnaise', 'pastrami']
finished_sandwiches = []
print("The deli has run out of pastrami. Eliminating errant sandwiches.")

pastrami_count = 0
while 'pastrami' in sandwich_orders:
    pastrami_count += 1
    print(f"Pastramis eliminated: {pastrami_count}")
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)

print("\nHere are your pastrami-less sandwiches. We weep with you.")
for sandwich in finished_sandwiches:
    print(f" - {sandwich.title()} sandwich")
