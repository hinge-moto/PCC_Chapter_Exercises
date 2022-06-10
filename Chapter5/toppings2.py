# April 23.2022

requested_toppings = ['']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    elif requested_topping != 'green peppers' and requested_topping != '':
        print("Adding " + requested_topping + ".")
    elif requested_toppings:
        print("Are you sure you want a plain pizza?")
    
print("\nFinished making your pizza!")


# Not yet sure what to do when line overruns character limit guide FUUUUUUUUUUUUUUUUU
# There needs to be something in the list for the for loop to run
# This is not optimal. What if the list is empty?
