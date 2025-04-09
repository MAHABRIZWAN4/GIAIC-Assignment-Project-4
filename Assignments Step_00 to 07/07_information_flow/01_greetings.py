# We've written a helper function for you called greet(name) which takes as input a string name and prints a greeting. Write some code in main() to get the user's name and then greet them, being sure to call the greet(name) helper function.


print("Step 07_INFORMATION_FLOW ==> 01_greetings")

def greet(name:str):
    print(f"'Hello Dear {name}' ! How are you? ")

def main():
    userName = input("Enter Your Name : ")
    greeting = greet(userName)


if __name__ == '__main__':
    main()