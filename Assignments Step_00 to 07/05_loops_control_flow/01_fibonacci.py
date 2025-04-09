# Write a program to print terms in the Fibonacci sequence up to a maximum value.



print("Step_05_LOOPS_CONTROL_FLOW ==> 01_fibonacci")


MAX_VALUE = 10000 

def main():
    a,b = 0,1
    print(a,b, end = " ")

    while True:
        c = a + b
        if c >= MAX_VALUE:
            break
        print(c, end=" ")
        a,b = b,c


if __name__ == "__main__":
    main()
