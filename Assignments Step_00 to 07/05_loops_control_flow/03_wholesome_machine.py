# Write a program which prompts the user to type an affirmation of your choice (we'll use "I am capable of doing anything I put my mind to.") until they type it correctly. Sometimes, especially in the midst of such uncertain times, we just need to be reminded that we are resilient, capable, and strong; this little Python program may be able to help!


print("Step_05_LOOPS_CONTROL_FLOW ==> 03_wholesome_machine")

def main():
    affirmation = "I am capable of doing anything I put my mind to."
    user_input = ""
    
    while user_input != affirmation:
        user_input = input("Type the affirmation: ")
        if user_input == affirmation:
            print("Correct! You are capable of doing anything you put your mind to.")
        else:
            print("Try again!")
if __name__ == "__main__":
    main()