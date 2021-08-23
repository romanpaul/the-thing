import random

# Calculates the dice roll for six sided dice of any number
def rolldice(number):
    dice = random.sample(range(1, 7), number)
    return dice
    
