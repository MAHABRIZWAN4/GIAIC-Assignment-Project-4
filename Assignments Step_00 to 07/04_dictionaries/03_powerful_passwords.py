# You want to be safe online and use different passwords for different websites. However, you are forgetful at times and want to make a program that can match which password belongs to which website without storing the actual password!

# This can be done via something called hashing. Hashing is when we take something and convert it into a different, unique identifier. This is done using a hash function. Luckily, there are several resources that can help us with this.



import hashlib

print("Step 04_dictionaries ==> 03_powerful_passwords")

def hash_password(password):
    """
    Hashes a password using SHA-256 and returns the hash.
    """
    return hashlib.sha256(password.encode()).hexdigest()

stored_logins = {
    "user@example.com": hash_password("password123"),
    "admin@example.com": hash_password("adminpass"),
}

def login(email, password):
    if email in stored_logins:
        return stored_logins[email] == hash_password(password)  # Call the function here
    return False

if __name__ == "__main__":
    email = input("Enter your email : ")
    password = input("Enter your password : ")


    if login(email , password):
        print("LOGIN SUCCESSFULLY")

    else:
        print("Invalid email or password")

