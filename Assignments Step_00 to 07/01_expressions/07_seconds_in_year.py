# Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print statement that looks like this (of course the value 5 should be the calculated number instead):

def main():
    print("Step01_expressions => 07_seconds_in_year")
    # Useful constants to help make the math easier and cleaner!
    Days_per_year: int = 365
    hour_per_day: int = 24
    min_per_hour: int = 60
    seconds_per_minutes: int = 60

    # Calculate the number of seconds in a year
    seconds_in_year: int = Days_per_year * hour_per_day * min_per_hour * seconds_per_minutes

    # Print the result in a nice format
    print(f"There are {seconds_in_year} seconds in a year.")

if __name__ == '__main__':
    main()