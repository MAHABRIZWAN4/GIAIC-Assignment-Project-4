import random
print("WELCOME TO ROCK , PAPER , SCISSOR GAME!")

choices = ["rock","paper","scissor"]

user_score = computer_score = 0

print("Let\'s play!")

while True:
    user_input = input("Type Rock , Paper , Scissor ot Q to quit : ").lower()
    if user_input == "q":
        print(f"Final Score - You : {user_score} , computer : {computer_score}")
        print("THANKS FOR PLAYING!")
        break
    if user_input not in choices:
        print("Invalid input, Please try again.")
        continue
    computer_choose = random.choice(choices)
    print(f"Computer Choose {computer_choose}.")
    if user_input == computer_choose:
        print("It's a tie!")
    elif (user_input == "rock" and computer_choose=="scissor") or (user_input == "paper" and computer_choose=="rock") or (user_input == "scissor" and computer_choose=="paper"):
        print("You Win!🎀🎉")
        user_score += 1
    else:
        print("Computer Wins!")
        computer_score += 1
        print(f"Current Score - you : {user_score} , Computer : {computer_score}")