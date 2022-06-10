# May 19.2022

class User:
    """Describes a human being."""

    def __init__(self, name, age, height, weight, hair):
        """Initialize the human."""
        self.name = name.title()
        self.age = age
        self.height = height
        self.weight = weight
        self.hair = hair

    def describe_user(self):
        """Prints a list of user attributes."""
        print(f"{self.name}'s attributes are:")
        print(f" - {self.age} years old")
        print(f" - {self.height}cm")
        print(f" - {self.weight}lbs")
        print(f" - {self.hair}")

    def greet_user(self):
        """Greet the human."""
        if self.weight < 200:
            print(f"\nHow do you do, {self.name}.\n")
        else:
            print(f"\nHow do you do, fatass.\n")

myself = User('dylan', 34, 195, 150, 'brown')
fatself = User('big dylan', 54, 195, 250, 'gray')

myself.describe_user()
myself.greet_user()

fatself.describe_user()
fatself.greet_user()
