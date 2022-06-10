# April 23.2022

age = 17.99

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")
    

# A more concise way of writing this code:

age_1 = 12

if age_1 < 4:
    price = 0
elif age_1 < 18:
    price = 5
else:
    price = 10
    
print("Your admission cost is $" + str(price) + ".")

# Remember you can ONLY concatenate strings, not integers
