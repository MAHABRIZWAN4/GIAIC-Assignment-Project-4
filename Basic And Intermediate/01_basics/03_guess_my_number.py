# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high


import random

print("Basic ==> 03_guess_my_number")

def main():
    randomNumber = random.randint(0,99)
    print("I am thinking of a number between 0 and 99")
    user_number = int(input("Enter a number what you guess ? "))
    
    while user_number != randomNumber:
        if user_number < randomNumber:
            print("Your guess is too Low 😫😜")
        else:
            print("Your guess is too High 😜")
        user_number = int(input("Enter a number what you guess ? "))

    print(f"Congratulations ! You guess a correct number {user_number}")




if __name__ == "__main__":
    main()
      
