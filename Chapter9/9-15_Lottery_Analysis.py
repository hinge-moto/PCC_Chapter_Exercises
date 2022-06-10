# May 21.2022

from random import choice

characters = [
            'a', 'f', 'w', 's', 'x',
            1, 22, 9, 54, 32, 81, 12, 44, 65, 4,
            ]


def lotto_pick():
    """Picks a random lottery ticket."""
    lottery_tic = []
    
    while len(lottery_tic) < 4:
        pick = choice(characters)
        if pick not in lottery_tic:
            lottery_tic.append(pick)

    return lottery_tic


def num_pulls_to_win(my_lotto=[]):
    """Returns the number of pulls until your ticket wins."""
    rand_tic = []
    i = 1

    print(f"Your ticket is {my_lotto}.")

    # Make the initial lottery draw:
    rand_tic = lotto_pick()

    # If our ticket does not match the last draw, redraw until it does:
    while my_lotto != rand_tic:
        rand_tic = []
        i += 1
        rand_tic = lotto_pick()

    print(f"It took {i} pulls until your lottery picks came up. LOSER.")


num_pulls_to_win(['f', 81, 9, 'a'])

# FUCK THIS WAS A NIGHTMARE BUT I CRUSHED IT...AFTER HOURS
# Ended up removing the entire class, a single function makes more sense here.
# Another rewrite...
# Annihilates the author's solution.
