# May 19.2022

def car_info(manuf, model, **other_info):
    """Prints a bunch of guff about a car."""
    other_info['manufacturer'] = manuf.title()
    other_info['model'] = model.title()
    return other_info

my_car = car_info('toyota', 'yaris',
                  color='red',
                  transmission='standard',
                  year=2012,
                  do_i_like='yes',
                  is_it_great=True,
                  )

print(my_car)
print()
for k, v in my_car.items():
    print(f"{k.title()}: {v}\n")
