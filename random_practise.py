# generating random values
import random


class Dice:
    def roll(self):
        first = random.randint(1,20)
        second = random.randint(1,20)
        return first, second
    

members = ['John','Mary','Johs','Sarah','Ivan','Singie','Leo','Wayne']
leader = random.choice(members)
for i in range(3):
    print(random.randint(10,20))

print(leader)
dice = Dice()
print(dice.roll())
