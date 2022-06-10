# April 22.2022


# Conditional tests for strings
##############################
if 'tool' == 'hammer':
    print("This tool is a hammer!")
else:
    print("This tool is not a hammer :(")


# Tests using lower()
####################
hammers = ['ball peen', 'claw', 'mallet', 'sledge']
best_hammer = 'sledge'

if best_hammer not in hammers:
    print("\nI hate these hammers!")
else:
    print("\nI love these hammers!")


# Boolean tests using numerals
#############################
family = 6
friends = 2

if family <= friends:
    print("\nToo many friends.")
else:
    print("\nCorrect number of friends.")


six = 6
eighty_eight = 88

if six < eighty_eight:
    print("\nMakes sense.")

if six == eighty_eight or six > eighty_eight:
    print("\nI mean honestly wtf.")
else:
    print("\nObjective truth")
    
# Already did the list tests BAZOOKA JOE GOOOOOOOO
#################################################
if hammers[1] == hammers[3]:
    print("\nNope.")
else:
    print("\nWell obviously.")
