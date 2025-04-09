# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.


print("Step 02_lists ==> 06_get_last_element")


def get_last_element(list):
    print(list[-1])

def get_list():
    list = []
    element = input("Enter the element that added to the list: ")
    while element != "":
        list.append(element)
        element = input("Enter the element that added to the list: ")
    return list
    
def main():
    list = get_list()
    get_last_element(list)


if __name__ == '__main__':
    main()
