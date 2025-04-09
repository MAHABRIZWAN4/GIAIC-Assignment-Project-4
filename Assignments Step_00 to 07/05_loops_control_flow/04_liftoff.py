# Write a program that prints out the calls for a spaceship that is about to launch. Countdown from 10 to 1 and then output Liftoff!




print("Step_05_LOOPS_CONTROL_FLOW ==> 04_liftoff")

def main():
    for i in range(10, 0 , -1):
        print(i, end=" ")  #  end=" " is ka mutlab he Har number ko space ke saath print karta hai (nayi line nahi aati).
    print("Liftoff!")

if __name__ == "__main__":
    main()