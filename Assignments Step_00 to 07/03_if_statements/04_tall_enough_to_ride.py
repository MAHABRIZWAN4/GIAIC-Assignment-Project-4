
# Write a program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.

# In amusement parks (ah, the good old pre-pandemic days...), rollercoasters frequently have minimum height requirements for safety reasons. Assume for now that the minimum height is 50 of whatever height unit you'd like 

print("Step03_IF_STATEMENT ==> 04_tall_enough_to_ride")


def tall_enough_extension():
    user_height = int(input("\033[1;3mHow tall are you ? Enter your height in inches: \033[0m"))

    min_height_for_ride = 50

    if user_height >= min_height_for_ride:
        print("You are tall enough to ride the roller coaster!")
    else:
        print("Sorry, you are not tall enough to ride the roller coaster.")
        print("You need to be at least", min_height_for_ride, "cm tall to ride the roller coaster.")


if __name__ == "__main__":
    tall_enough_extension()