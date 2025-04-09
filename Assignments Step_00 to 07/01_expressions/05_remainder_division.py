# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

def main():
    print("Step01_expressions => 05_division_remainder")
    num1 = float(input("\033[1;3mEnter the first number: \033[0m"))
    num2 = float(input("\033[1;3mEnter the second number: \033[0m"))
    division = num1 / num2 
    remainder = num1 % num2
    print(f"The division of the given is {division} and the remainder is {remainder}.")

if __name__ == '__main__':
    main()