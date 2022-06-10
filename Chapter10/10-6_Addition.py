# May 23.2022

print("Please press 'q' to quit.")
while True:
    augend = input("Please enter the augend: ")
    if augend == 'q':
        break
    addend = input("Please enter the addend: ")
    if addend == 'q':
        break
    try:
        total = int(augend) + int(addend)
    except ValueError:
        print("Please enter an integer.")
    else:
        print(total)
