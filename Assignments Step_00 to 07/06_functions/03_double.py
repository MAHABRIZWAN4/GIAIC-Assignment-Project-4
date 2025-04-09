# Fill out the double(num) function to return the result of multiplying num by 2. We've written a main() function for you which asks the user for a number, calls your code for double(num) , and prints the result.

print("Step 06_FUNCTIONS ==> 03_double")

def double(num):
    return num *  2

def main():
    # Get a number from the user
    num = float(input("Enter a number: "))

    # Call the function to double the number
    result = double(num)

    # Print the result
    print(f"The double of {num} is {result}.")



if __name__ == "__main__":
    main()