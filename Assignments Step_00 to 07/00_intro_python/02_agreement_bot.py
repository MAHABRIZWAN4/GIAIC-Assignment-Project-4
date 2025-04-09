# Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

def main():
    pink_color = "\033[95m"
    reset_color = "\033[0m"
    yellow_color = "\033[93m"
    
    ask_user = input(f"\033[1;3m{pink_color} What is your favorite animal? {reset_color}\033[0m")
    print(f"{yellow_color}My favorite animal is also {pink_color}{ask_user}!")  

if __name__ == '__main__':
    main()

# Ye bold blue or pink kerne to ansi excape code he .