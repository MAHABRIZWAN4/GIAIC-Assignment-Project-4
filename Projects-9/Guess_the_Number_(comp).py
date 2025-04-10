import random
print("WELCOME TO MY NUMBER GUESSING GAME THAT COMPUTER GUESS THE NUMBER 🤗🤩")

low = 1
high = 100


print("Think of a number betweeb 1 to 100 and the computer guess it : ")


if low <= high:
    guess = random.randint(low , high)
    print(f"Computer guess number is : {guess}")

    while True:
        feedback = input("IS THE GUESS TOO HIGH ( H ) , TOO LOW ( L ) OR CORRECT ( C ) :  ")

        if feedback == "C":
            print("Hurray 🎉 The Computer guessed your number .")
            break
        elif feedback == "H":
            high = guess - 1
            guess = random.randint(1,100)
            print(f"Computer's guess number is {guess}") 
        elif feedback == "L":
            high = guess + 1
            guess = random.randint(1,100)
            print(f"Computer's guess number is {guess}") 
        else:
            print("Please choose only 'H' , 'L' or 'C'!!")
             

if low > high:
    print("The number is not in the range .. Please try again .")





