# May 19.2022

class Restaurant:
    """A simple modeling of a generic restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        "Initialize restaurant's name and cuisine."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints our two attributes."""
        print(f"\n{self.restaurant_name} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        """Prints that the restaurant is open."""
        print(f"\n{self.restaurant_name} is open!")

new_restaurant = Restaurant('Curries and Puffs', 'Indian')
old_restaurant = Restaurant("Albert's", 'basic')
space_restaurant = Restaurant('The Black Hole', 'nutrient paste')

new_restaurant.describe_restaurant()
old_restaurant.describe_restaurant()
space_restaurant.describe_restaurant()
