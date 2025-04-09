# Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).



def main():
    side1_input = int(input(("Enter the length of triangle side1 : ")))
    side2_input = int(input(("Enter the length of triangle side2 : ")))
    side3_input = int(input(("Enter the length of triangle side3 : ")))
    
    Perimeter = side1_input + side2_input + side3_input
    print(f"The perimeter of the triangle is {Perimeter}")

if __name__ == '__main__':
    main()






