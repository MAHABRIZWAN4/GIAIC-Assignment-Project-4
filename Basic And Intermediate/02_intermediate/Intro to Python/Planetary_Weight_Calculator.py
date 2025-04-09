# A few years ago, NASA made history with the first controlled flight on another planet. Its latest Mars Rover, Perseverance, has onboard a 50cm high helicopter called Ingenuity. Ingenuity made its third flight, during which it flew faster and further than it had on any of its test flights on Earth. Interestingly, Ingenuity uses Python for some of its flight modeling software!

# Ingenuity on the surface of Mars (source: NASA)

# When programming Ingenuity, one of the things that NASA engineers need to account for is the fact that due to the weaker gravity on Mars, an Earthling's weight on Mars is 37.8% of their weight on Earth. Write a Python program that prompts an Earthling to enter their weight on Earth and prints their calculated weight on Mars.

# The output should be rounded to two decimal places when necessary. Python has a round function which can help you with this. You pass in the value to be rounded and the number of decimal places to use. In the example below, the number 3.1415926 is rounded to 2 decimal places which is 3.14.



print("Intermediate ==> Planetary Weight Calculator")




print("*****************************")
print("*****************************")
print("Welcome to the Planetary Weight Calculator!")
print("*****************************")
print("*****************************")



def main():
    your_weight = float(input("Enter your weight on earth : "))


    gravity_ratios = {
        "Mercury": 0.38,
        "Venus": 0.91,
        "Mars": 0.38,
        "Jupiter": 2.34,
        "Saturn": 1.06,
        "Uranus": 0.92,
        "Neptune": 1.19,

    }

    print("\n Please Select a Planet : ")


    for planet in gravity_ratios:
        print(f"- {planet}")

    planet_choice = input("Enter the name of the planet : ").title()


    if planet_choice in gravity_ratios:
        new_weight = your_weight * gravity_ratios[planet_choice]
        print(f"Your weight on {planet_choice} is {new_weight:.2}Kg")
    else:
        print("Invalid Planet Choice .. Please a correct planet 🔴")




if __name__ == "__main__":
    main()
