# Write a function called print_ones_digit , which takes as a parameter an integer num and prints its ones digit. The modulo (remainder) operator, %, should be helpful to you here. Call your function from main()!


print("Step 06_FUNCTIONS ==> 09_print_ones_digit")


def print_ones_digit(num:int):
    ones_digit = num % 10 
    print(f"The ones digit is {ones_digit}")


def main():
    numberInput = int(input("\033[34mEnter the Number : \033[0m"))
    print_ones_digit(numberInput)
    

if __name__ == "__main__":
    main()