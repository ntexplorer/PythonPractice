import random


def coin_flip():
    Heads = 0
    Tails = 0
    flip_num = int(input("How many times do you want to flip the coins: "))
    while flip_num > 0:
        flip = random.randint(0, 1)
        if flip == 1:
            Heads += 1
        else:
            Tails += 1
        flip_num -= 1
    print("The number of Heads is: " + str(Heads) + ".")
    print("The number of Tails is: " + str(Tails) + ".")


coin_flip()
