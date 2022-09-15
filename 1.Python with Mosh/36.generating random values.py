import random

for i in range(3):
    print(random.random())
    print(random.randint(10,30))

members = ["Mohammad","Jonayed","sarkar"]

print(random.choice(members))


class Dice:
    def roll(self):
        x = random.randint(1,5)
        y = random.randint(1,5)
        print(f"({x},{y})")


number = Dice()
number.roll()