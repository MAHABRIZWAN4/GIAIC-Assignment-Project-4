# Simulate rolling two dice, and prints results of each roll as well as the total.


import random
print("Step01_expressions => 06_rolldice")

def roll_dice():
    die1:int = random.randint(1,6)
    die2:int = random.randint(1,6)
    print(f"Die1: {die1} , Die2: {die2}")
    total:int = die1 + die2
    print(f"The total of two dies is {total}") 

if __name__ == '__main__':
    roll_dice()