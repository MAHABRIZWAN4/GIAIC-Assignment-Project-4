# Write a function that takes two numbers and finds the average between the two.


print("Step 06_FUNCTIONS ==> 00_average")

def calculate_average(num1, num2):
    
    # Calculate the average of two numbers.

    # Parameters:
    # num1 (float): The first number.
    # num2 (float): The second number.

    # Returns:
    # float: The average of the two numbers.
    
    return (num1 + num2) / 2


def main():
    # Get two numbers from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Call the function to calculate the average
    average = calculate_average(num1, num2)

    # Print the result
    print(f"The average of {num1} and {num2} is {average}.")

if __name__ == "__main__": 
    main()