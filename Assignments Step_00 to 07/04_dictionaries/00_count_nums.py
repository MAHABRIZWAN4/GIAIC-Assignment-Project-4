# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.



print("Step 04_dictionaries ==> 00_count_nums")

def count_numbers():
    count_dict = {}

    while True:
        num = input("Enter a number or Exit to stop: ")  # Keep input as a string
        if num.title() == "Exit":  # Check if the input is "Exit"
            break
        if num.isdigit():  # Check if the input is a valid number
            num = int(num)  # Convert to integer
            count_dict[num] = count_dict.get(num, 0) + 1
        else:
            print("Please enter a valid number or 'Exit'.")
    
    return count_dict  # Ensure this is outside the loop

def display_count(count_dict):
    print("Number counts:")
    for key, value in count_dict.items():
        print(f"{key} appears {value} times.")



if __name__ == "__main__":
    count_dict = count_numbers()
    display_count(count_dict)