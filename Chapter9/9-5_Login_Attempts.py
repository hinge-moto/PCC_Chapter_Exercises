# May 20.2022

class User:
    """Describes a human being."""

    def __init__(self, name, age, height, weight, hair):
        """Initialize the human."""
        self.name = name.title()
        self.age = age
        self.height = height
        self.weight = weight
        self.hair = hair
        self.mutilate_attempts = 0

    def describe_user(self):
        """Prints a list of human attributes."""
        print(f"{self.name}'s attributes are:")
        print(f" - {self.age} years old")
        print(f" - {self.height}cm")
        print(f" - {self.weight}lbs")
        print(f" - {self.hair}")
        print(f" - {self.mutilate_attempts} attempts at self-mutilation.")

    def greet_user(self):
        """Greet the human."""
        if self.weight < 200:
            print(f"\nHow do you do, {self.name}.\n")
        else:
            print(f"\nHow do you do, fatass.\n")

    def increment_by1_mutilate_attempts(self):
        """Increment the number of attempts at self-mutilation by 1."""
        self.mutilate_attempts += 1
        print(f"\nSelf-mutilating... {myself.mutilate_attempts}")

    def reset_mutilate_attempts(self):
        """Resets the number of self-mutilations to 0."""
        self.mutilate_attempts = 0
        print(f"\nResetting mutilation attempts: {myself.mutilate_attempts}")

myself = User('dylan', 34, 195, 150, 'brown')

myself.describe_user()

print(f"\nI have self-mutilated {myself.mutilate_attempts} times today.")

myself.increment_by1_mutilate_attempts()
myself.increment_by1_mutilate_attempts()
myself.increment_by1_mutilate_attempts()
myself.increment_by1_mutilate_attempts()
myself.increment_by1_mutilate_attempts()

myself.reset_mutilate_attempts()
