# April 20.2022

for value in range(1, 16):
    print(value)


numbers = list(range(1, 11, 2))
print(numbers)


square_numbers = []
for number in range(1,11):
    square = number**2
    square_numbers.append(square) # or just: square_numbers.append(value**2)
    
print(square_numbers)
