# May 21.2022

from just_admin import User

"""A set of classes that describe an admin."""

class Priveleges:
    """Sets the priveleges for a user."""
    
    def __init__(self):
        self.priveleges = [
            'can add post',
            'can delete post',
            'can edit post',
            'can ban user',
            'can approve user',
            ]

    def show_priveleges(self):
        """Prints a list of admin priveleges."""
        print(f"\nThe admin has these incredible powers:")
        for privelege in self.priveleges:
            print(f" - {privelege}")


class Admin(User):
    """Models the admin, taking after the user."""

    def __init__(self, name, age, height, weight, hair):
        """Initialize the admin's details."""
        super().__init__(name, age, height, weight, hair)
        self.priveleges = Priveleges()
