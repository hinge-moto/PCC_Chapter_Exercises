# May 14.2022

fav_num = {
    'harry': [3, 666],
    'larry': [8],
    'garry': [6, 21],
    'hank': [1],
    'neptune': [0],
    'flo': [99, 100,000,000,000],
    }

for name, numbers in fav_num.items():
    if len(numbers) > 1:
        print(f"\n{name.title()}'s favourite numbers are:")
        for number in numbers:
            print(f"  {number}")
    else:
        print(f"\n{name.title()}'s favourite number is:\n  {number}")
