# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.



print("Step 02_lists ==> 05_get_first_element")


def get_first_element(list):
    print(list[0])

def get_list():
    list = []
    element = input("Enter the element that added to the list: ")
    while element != "":
        list.append(element)
        element = input("Enter the element that added to the list: ")
    return list
    
def main():
    list = get_list()
    get_first_element(list)


if __name__ == '__main__':
    main()
