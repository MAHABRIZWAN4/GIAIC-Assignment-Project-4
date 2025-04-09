# Print 10 random numbers in the range 1 to 100.

import random

print("Step03_IF_STATEMENT ==> 05_random_numbers")


def random_numbers():
    print("Random number between 1 and 100:")
    for i in range(10):
        random_numbers = random.randint(1,100)
        print(random_numbers)

if __name__ == "__main__":
    random_numbers()