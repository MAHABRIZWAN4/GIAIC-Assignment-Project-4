# Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to call the subtract_seven helper function! If you're stuck, revisit the add_five example from lecture.


print("Step 07_INFORMATION_FLOW ==> 05_subtract_7.")



def subtract_seven(num: int):
    # Subtract 7 from the given number and return the result
    return num - 7

def main():
    # Take user input for the number
    number = int(input("Enter a number: "))
    
    # Call the subtract_seven function and print the result
    result = subtract_seven(number)
    print(f"The result after subtracting 7 is: {result}")

if __name__ == '__main__':
    main()
