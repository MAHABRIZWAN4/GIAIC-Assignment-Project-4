# Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.



print("Basic ==> 01_double_it")

def main():
    user_input = int(input("Enter a number ? "))
    while user_input < 100:
        user_input = user_input * 2
        print(user_input)

if __name__ == "__main__":
    main()
