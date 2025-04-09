# Guess My Number


import random

print("Step_05_LOOPS_CONTROL_FLOW ==> Guess My Number")

def guess_my_number():
    
    guess_number = random.randint(0, 99)
    
    user_guess = int(input("I am thinking of a number between 0 and 99 :"))

    while True:
        if guess_number < user_guess:
            print("Too high!")
            user_guess = int(input("Try again: "))
        elif guess_number > user_guess:
            print("Too low!")
            user_guess = int(input("Try again: "))
        else:
            print("Congratulations! You guessed the correct number!")
            break


if __name__ == "__main__":
    guess_my_number()