# Fill out print_multiple(message, repeats), which takes as parameters a string message to print, and an integer repeats number of times to print message. We've written the main() function for you, which prompts the user for a message and a number of repeats.



print("Step 06_FUNCTIONS ==> 07_print_multiple")

def print_multiple(message, repeats):
  
  
    for _ in range(repeats):  # Loop runs 'repeats' number of times
        print(message)

def main():
    # User input
    message = input("\033[34mPlease type a message: \033[0m")  
    repeats = int(input("Enter a number of times to repeat your message: "))  # Convert to integer
    
    # Call the print_multiple function
    print_multiple(message, repeats)

if __name__ == '__main__':
    main()
