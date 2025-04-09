# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.

import random
print("Step01_expressions => 01_dicesimulator")



def roll_dice():
    die1:int = random.randint(1,6)
    die2:int = random.randint(1,6)
    total:int = die1 + die2
    print(f"The total of two dies is {total}") 


def main():
    die1:int = 14
    print(f"Die1 in main()function is equal to {die1}")
    roll_dice()
    roll_dice()
    roll_dice()
    roll_dice()
    roll_dice()

    print(f"Die1 in main()function is equal to {die1}")



#    ye type guard he hum is me make sure kerte hein ke ye function sirf tabhi chale jab hmum isay call kerwayein warna to ye import hote ke sath hi execute ho jata hai
if __name__ == '__main__':
    main()


              