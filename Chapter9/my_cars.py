# May 21.2022

from car import Car
from electric_car import ElectricCar as EC

my_beetle = Car('Volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = EC('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
