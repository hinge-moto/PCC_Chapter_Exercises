# May 21.2022

"""A class that can be used to represent a car."""

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
        self.odometer += miles # += means to combine
