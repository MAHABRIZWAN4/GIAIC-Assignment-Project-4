# Create a Python program that helps you practice accessing and manipulating elements in a list. This exercise will help you get comfortable with indexing, slicing, and modifying list elements.



print("Intermediate ==> Index Game")




print("*****************************")
print("*****************************")
print("Welcome To My List Game!")
print("*****************************")
print("*****************************")


my_list = ["apple","mango","orange","pear","peach"]

def access_element(my_list,index):
    if 0 <= index < len(my_list):
        return f"Element at index {index}: {my_list[index]}"
    return "Index out of range"



def modify_element(my_list,index,new_value):
    if 0 <= index < len(my_list):
        old_value= my_list[index]
        my_list[index] = new_value
        return f"Element at index {index} modified form {old_value} to {new_value}"
    return "Index out of range"



def slice_list(my_list,start,end):
    if 0 <= start < len(my_list) and 0 <= end <= len(my_list):
        return f"Sliced List: {my_list[start:end]}"
    return("Invalid slice indicates!!")



def list_game():
    my_list = ["apple","mango","orange","pear","peach"]

    while True:
        print("Current List" , my_list)
        print("Select an operation")
        print("1. Access Element")
        print("2. Modify Element")
        print("3. Slice Test")
        print("4. Quit")
        
        Choice = input("Enter your choice (1-4) : ")

        if Choice == "1":
            index = int(input("Enter the index of the element you want to access : "))
            print(access_element(my_list,index))
        
        if Choice == "2":
            index = int(input("Enter the index of the element you want to modify : "))
            new_value = input("Enter the new value for the element : ")
            print(modify_element(my_list,index, new_value))

        elif Choice == "3":
            start = int(input("Enter the start index from the slice: "))
            end = int(input("Enter the end index from the slice: "))
            print(slice_list(my_list,start,end))
        elif Choice == "4":
            print("Existing the game, Thanks For Playing..")
            break
        else:
            print("Invalid Choice! Please enter a number betweeb 1 to 4 !!")

        


if __name__ == "__main__":
    list_game()
