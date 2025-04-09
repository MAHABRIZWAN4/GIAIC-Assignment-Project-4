# Fill out the function count_even(lst) which first populates a list by prompting the user for integers until they press enter (please use the prompt "Enter an integer or press enter to stop: "), and then prints the number of even numbers in the list.


print("Step 06_FUNCTIONS ==> 02_count_even")

def count_even():
    list  = []
    while True:
        num = input("Enter an integer or press enter to stop: ")
        if num == "":
            break
        else:
            list.append(int(num))


    count = 0
    for number in list:
        if number % 2 == 0:
            count += 1

            
    print("Number of even numbers:", count)


if __name__ == "__main__":
    count_even()