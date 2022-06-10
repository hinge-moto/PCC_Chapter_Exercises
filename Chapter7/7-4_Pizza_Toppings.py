# May 15.2022

toppings = "\nPlease add your next topping."
toppings += "\nEnter 'quit' to complete your pizza: "

while True:
    pizza = input(toppings)
    toppings_list = []
    
    if pizza == 'quit':
        break
    else:
        toppings_list.append(pizza)
        print(toppings_list)

# Don't know how to make this work.
