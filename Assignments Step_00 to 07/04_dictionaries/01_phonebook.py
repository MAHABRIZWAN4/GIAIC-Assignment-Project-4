# In this program we show an example of using dictionaries to keep track of information in a phonebook.



print("Step 04_dictionaries ==> 01_phonebook")



def add_contact(phonebook):
    name = input("Enter the name:")
    number = int(input("Enter the number:"))

    if name in phonebook:
        print("Contact already exists.")
    else:
        phonebook[name] = number
        print("Contact added successfully.")


def search_contact(phonebook):
    name = input("Enter the name to search:")
    if name in phonebook:
        print(f"{name}'s number is {phonebook[name]}")
    else:
        print("Contact not found.")



def delete_contact(phonebook):
    name = input("Enter the name to delete:")
    if name in phonebook:
        del phonebook[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def display_contacts(phonebook):
    if phonebook:
        print("\n Phonebook contacts List:")
        for name, number in phonebook.items():
            print(f"{name}: {number}")
    else:
        print("No contacts in the phonebook.")



if __name__ == "__main__":
    phonebook = {}
    while True:
        print("\nPhonebook Menu:")
        print("1. Add contact")
        print("2. Search contact")
        print("3. Delete contact")
        print("4. Display contacts")
        print("5. Exit")

        choice = input("Enter your choice:")

        if choice == "1":
            add_contact(phonebook)
        elif choice == "2":
            search_contact(phonebook)
        elif choice == "3":
            delete_contact(phonebook)
        elif choice == "4":
            display_contacts(phonebook)
        elif choice == "5":
            break
        else:
            print("Invalid choice, please try again.")