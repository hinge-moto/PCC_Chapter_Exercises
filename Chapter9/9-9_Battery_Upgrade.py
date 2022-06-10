# May 20.2022

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to represent a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"\n{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print the car's mileage."""
        print(f"This car has {self.odometer} miles on it.")

    def update_odometer(self, mileage):
        """
        Update the odometer reading.
        Reject the change if it is less than the current reading.
        """
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("You can't roll back the odometer!")

    def increment_odometer(self, miles):
        """Increment the odometer."""
        self.odometer += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def upgrade_battery(self, capacity=100):
        """Upgrades the battery's capacity."""
        if self.battery_size < 100:
            print("Upgrading your battery!")
            self.battery_size = 100

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")
        

class ElectricCar(Car): # This child class must appear after parent class.
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery() # Battery instance, stored in this variable.

my_electric_car = ElectricCar('chevy', 'bolt', 2022)
my_electric_car.battery.get_range()
my_electric_car.battery.upgrade_battery()
my_electric_car.battery.get_range()
