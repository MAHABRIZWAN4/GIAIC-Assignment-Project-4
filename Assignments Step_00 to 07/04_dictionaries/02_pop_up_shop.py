# There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time, you want to keep track of how much the fruit will cost before you go. Luckily you wrote down what fruits were available and how much one of each fruit costs.

# Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.

print("Step 04_dictionaries ==> 02_pop_up_shop")


def calculate_total_cost():
    fruit_prices = {
        "apple": 5.0,
        "banana": 2.0,
        "orange": 3.0,
        "grape": 4.0,
        "kiwi": 2.0,
        "mango": 6.0,
        "watermelon": 8.0,
        "peach": 4.0,
        "pineapple": 7.0,
        "strawberry": 3.0,
    }
    total_cost = 0.0

    for fruit, price in fruit_prices.items():
        while True:
            try:
                quantity = int(input(f"How many {fruit}s do you want to buy? "))
                if quantity < 0:
                    print("Please enter a positive number.")
                    continue
                total_cost += price * quantity
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
                

    print("\nThank you for shopping with us!")
    print("===================================")

    print("Here is your receipt:")
    print("===================================")
    print("===================================")
    for fruit, price in fruit_prices.items():
        print(f"Fruit: {fruit}, Quantity: {quantity}, Price per unit: {price} rupees")
    print(f"The total cost of your fruits is: ${total_cost:.2f}")
                
          

if __name__ == "__main__":
    calculate_total_cost()