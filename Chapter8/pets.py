# May 16.2022 - Positional Arguments

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'hammy')
describe_pet('cat', 'newt')


# or.... Keyword Arguments
describe_pet(animal_type='hamster', pet_name='harry')


# Using Default Values (must use right position, even here)
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='bowie')
describe_pet('rufus')
