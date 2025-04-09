# Write a function that takes a list of numbers and returns the sum of those numbers.

print("Step 02_lists ==> 01_add_many_number")

def sum_of_number(numbers) -> int:
    num: int = 0
    for i in numbers:
        num += i
    return num  

def main():
    list_of_numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sum = sum_of_number(list_of_numbers)

    print(f"The sum of {list_of_numbers} is {sum}.")

if __name__ == '__main__':
    main()

