# Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.


print("Step_05_LOOPS_CONTROL_FLOW ==> 05_double_it")


def main():
    number = int(input("Enter a number that will be doubled until it becomes 100 or more:"))
    while number < 100: #Jab tak number 100 se chhota hai, tab tak neeche wali lines baar baar chalti rahengi.
        number = number * 2
        print(number)

if __name__ == "__main__":
    main()




                                        