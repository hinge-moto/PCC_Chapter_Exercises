# April 27.2022

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
            print(f"\t{number}")
    else:
        print(f"\n{name.title()}'s favourite number is:\n\t{number}")




##num = fav_num['harry']
##print(f"Harry's favourite number is {num}.")
##
##num = fav_num['larry']
##print(f"Larry's favourite number is {num}.")
##
##num = fav_num['garry']
##print(f"Garry's favourite number is {num}.")
##
##num = fav_num['hank']
##print(f"Hank's favourite number is {num}.")
##
##num = fav_num['neptune']
##print(f"Neptune's favourite number is {num}.")
##
##num = fav_num['flo']
##print(f"Flo's favourite number is {num}.")
