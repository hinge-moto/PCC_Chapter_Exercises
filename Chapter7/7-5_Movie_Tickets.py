# May 15.2022

prompt = "\nTicket price is based on age."
prompt += "\nPlease enter your age: "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("Your ticket is free!")
    elif age < 12:
        print("Your ticket is $10")
    else:
        print("Your ticket is $15")
