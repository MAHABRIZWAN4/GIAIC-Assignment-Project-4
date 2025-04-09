# Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.


print("Step 02_lists ==> 07_get_list")


def get_full_list(list):
    print(list)

def get_list():
    list = []
    element = input("Enter the element that added to the list: ")
    while element != "":
        list.append(element)
        element = input("Enter the element that added to the list: ")
    return list
    
def main():
    list = get_list()
    get_full_list(list)


if __name__ == '__main__':
    main()
