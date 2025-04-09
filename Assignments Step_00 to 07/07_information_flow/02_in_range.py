# Implement the following function which takes in 3 integers as parameters:

# def in_range(n, low, high) """ Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low. """

print("Step 07_INFORMATION_FLOW ==> 02_in_range")

def in_range(n, low, high): 
     if n >= low and n <= high:
          return True
     else:
          return False


def main():
    # Getting input for the number, low, and high
    n = int(input("Enter the number: "))
    low = int(input("Enter the low value: "))
    high = int(input("Enter the high value: "))
    
    # Calling the in_range function with the inputs
    result = in_range(n, low, high)
    print(result)


if __name__ == "__main__":
     main()
