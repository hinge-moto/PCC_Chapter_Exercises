# May 21.2022

from random import randint


class Die:
    """Defines a die(dice) with a certain number of sides."""
    
    def __init__(self, sides=6):
        """Initializes an 'n' sided die."""
        self.sides = sides

    def roll_die(self):
        """Returns the value of the die roll."""
        return randint(1,self.sides)


six_die = Die()
ten_die = Die(10)
twenty_die = Die(20)

for roll in range(1,11):
    print(six_die.roll_die())
    if roll == 10:
        print()

for roll in range(1,11):
    print(ten_die.roll_die())
    if roll == 10:
        print()
        
for roll in range(1,11):
    print(twenty_die.roll_die())
    if roll == 10:
        print()
