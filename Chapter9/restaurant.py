# May 21.2022

"""A class that can be used to represent a restaurant."""

class Restaurant:
    """A simple modeling of a generic restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        "Initialize restaurant's name and cuisine."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Prints our restaurant's attributes."""
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        """Prints that the restaurant is open."""
        print(f"{self.restaurant_name} is open!")

    def set_number_served(self, served):
        """Set the number of customers that have been served."""
        if self.number_served <= served:
            self.number_served = served
        else:
            print("You can never go baaaaaack.")

    def increment_number_served(self, served):
        """Increment the number of customers served."""
        self.number_served += served
