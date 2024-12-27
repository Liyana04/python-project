# generating random values
import random
# pathlib
from pathlib import Path

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


#Absolute path
#c:\Program Files\Microsoft
# /usr/local/bin
# Relative Path

path = Path("ecommerce")
print(path.exists())
# create a directory
# print(path.mkdir())
# remove a directory
# print(path.rmdir())
# find directory in different path
for file in path.glob('*.py'):
    print(file)