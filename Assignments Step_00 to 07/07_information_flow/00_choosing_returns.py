# There are times where we want to return different things from a function based on some condition. To practice this idea, imagine that we want to check if someone is an adult. We might check their age and return different things depending on how old they are!



print("Step 07_INFORMATION_FLOW ==> 00_choosing_returns")


ADULT_AGE = 18

def is_adult(age):
    
    if age >= ADULT_AGE:
        return True  
    else:
        return False  
def main():
    age = int(input("How old is this person?: "))
    print(is_adult(age))  # True ya False print hoga based on age

if __name__ == '__main__':
    main()
