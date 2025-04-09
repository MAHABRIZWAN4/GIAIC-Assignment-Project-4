# There are times where you are working with lots of different data within a function that you want to return. While generally, we want to keep functions to have a precise purpose, sometimes that purpose just deals with multiple bits of data.


print("Step 07_INFORMATION_FLOW ==> 04_multiple_returns")

def get_user_data():
   
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    email = input("What is your email address?: ")
    
   
    return first_name, last_name, email

def main():
    
    user_data = get_user_data()
    
    
    print(f"Received the following user data: {user_data}")

if __name__ == '__main__':
    main()
