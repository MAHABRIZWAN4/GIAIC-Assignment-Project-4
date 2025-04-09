# Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.

def main():
    fahrenheit = int(input("\033[1;3mEnter temperature in Fahrenheit (°F): \033[0m"))

    celsius =  (fahrenheit - 32) * 5.0/9.0
    print(f"Temperature in Celsius is: {celsius}°C")

if __name__ == '__main__':
    main()











    