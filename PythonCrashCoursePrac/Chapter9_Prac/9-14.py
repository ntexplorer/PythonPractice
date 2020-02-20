from random import randint


class Die():
    def __init__(self):
        self.sides = 6

    def roll_die(self):
        result = randint(1, self.sides)
        print(result)

    def set_sides(self, side_num):
        self.sides = side_num


die1 = Die()
i = 1

while i <= 10:
    die1.roll_die()
    i += 1

print("#############")

die2 = Die()
die3 = Die()
die2.set_sides(10)
die3.set_sides(20)

n = 0
while n <= 10:
    die2.roll_die()
    die3.roll_die()
    n += 1
