import random


def randomNumber(rightBorder, includeZero=False):
    if includeZero:
        return random.randint(0-rightBorder, rightBorder)
    else:
        plusOrMinus = random.randint(0, 1)
        if plusOrMinus == 0:
            return random.randint(1, rightBorder)
        else:
            return 0 - random.randint(1, rightBorder)
