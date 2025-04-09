# Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!


def main():
    print("Step01_expressions => 04_pythagorean_theorem")
    length_1 = float(input("Enter the length of the LM (Base) : "))
    length_2 = float(input("Enter the length of the LN (Perpendicular) : "))
    length_3 = (length_1 ** 2 + length_2 ** 2) ** 0.5
    print(f"The length of the MN ( hypotenuse ) is {length_3}.")

if __name__ == '__main__':
    main()