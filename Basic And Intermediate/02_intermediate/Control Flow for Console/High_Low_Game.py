# We want you to gain more experience working with control flow and Booleans in Python. To do this, we are going to have you develop a game! The game is called High-Low and the way it's played goes as follows:

# Two numbers are generated from 1 to 100 (inclusive on both ends): one for you and one for a computer, who will be your opponent. You can see your number, but not the computer's!

# You make a guess, saying your number is either higher than or lower than the computer's number

# If your guess matches the truth (ex. you guess your number is higher, and then your number is actually higher than the computer's), you get a point!

# These steps make up one round of the game. The game is over after all rounds have been played.

import random 

print("Intermediate ==> High-Low Game")

round = 5

def main():
    print("*****************************")
    print("*****************************")
    print("Welcome to the High-Low Game!")
    print("*****************************")
    print("*****************************")

    your_score = 0

    for i in range(round):
        print("Round" , i + 1)

        computer_number:int = random.randint(1,100)
        your_number:int = random.randint(1,100)
        print(f"Your Number is { your_number}")

        choice = input("Do you think your number is higher or lower than the computer's number ? ")
        higher_and_correct  = choice == "higher" and your_number > computer_number
        lower_and_correct  = choice == "lower" and your_number < computer_number


        if higher_and_correct or lower_and_correct:
            print(f"Awesome✨🎉 You were right! The computer's number was {computer_number}")
            your_score += 1

        else:
            print(f"Ohooo🎃, that's incorrect. The computer's number was  {computer_number}")

        print(f"Your Score🎖 is now :  {your_score}")
        print()
        print("Thanks For Playing this game .. Welcome Anytime ⏳")


if __name__ == "__main__":
    main()