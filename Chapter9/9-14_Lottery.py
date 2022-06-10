# May 21.2022

from random import randint, choice

class LotteryTicket:
    """Describes a lottery ticket made of letters and numbers."""

    def __init__(self):
        """Initializes the lottery ticket."""
        self.characters = [
            'a', 'f', 'w', 's', 'x',
            1, 22, 9, 54, 32, 81, 12, 44, 65, 4,
            ]

    def lotto_pick(self):
        """Randomly chooses four characters from the list."""
        self.lotto_pick = []
        
        while len(self.lotto_pick) < 4:
            pick = choice(self.characters)
            if pick not in self.lotto_pick:
                self.lotto_pick.append(pick)
                
        print("And the winning picks are.....")
        for pick in self.lotto_pick:
            print(f" {pick}")
            
            
my_ticket = LotteryTicket()

my_ticket.lotto_pick()
