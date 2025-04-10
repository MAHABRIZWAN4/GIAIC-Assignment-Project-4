import random
import string

def generate_password(length):
    if length < 6:
        return "Password must be at least 6 characters long."

    characters = string.ascii_letters + string.digits + string.punctuation

    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

try:
    user_length = int(input("Enter the length of the password: "))
    password = generate_password(user_length)
    print(f"Generated Password: {password}")
except ValueError:
    print("Please enter a valid number.")
