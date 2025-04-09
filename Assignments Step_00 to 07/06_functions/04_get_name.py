# Fill out the get_name() function to return your name as a string! We've written a main() function for you which calls your function to retrieve your name and then prints it in a greeting.

print("Step 06_FUNCTIONS ==> 04_get_name")


def get_name(name:str):
    return name



def main():
    Name = input("Enter Your Name: ")
    name= get_name(Name)
    geeting = print(f"Hi Dear {name}")


if __name__ == "__main__":
    main()
