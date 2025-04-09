# Write the helper function print_divisors(num), which takes in a number and prints all of its divisors (all the numbers from 1 to num inclusive that num can be cleanly divided by (there is no remainder to the division). Don't forget to call your function in main()!


print("Step 06_FUNCTIONS ==> 06_print_divisor")

def print_divisors(num):
    print(f"Here are the divisors of {num}:")
    for i in range(1, num+1):  # 1 se lekar num tak numbers check karenge
        if num % i == 0:  # Agar num ko i se divide karne par remainder 0 mile
            print(i, end=" ")  # i ko print kar do
    print()  # line break ke liye


def main():
    num = int(input("\033[34mEnter a number: \033[0m"))  # User se number lena
    print_divisors(num)  # Function ko call karna



if __name__ == '__main__':
    main()