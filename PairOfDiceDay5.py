import random

rolls: int = input("Input the number of times you'd like to simulate rolling a pair of dice [input a negative number to quit]: ")
rolls = int(rolls)

while rolls >= 0:
    for i in range(rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        print(f"Roll {i + 1}: {die1} + {die2} = {total}")
    rolls = input("Input the number of times you'd like to simulate rolling a pair of dice [input a negative number to quit]: ")
    rolls = int(rolls)