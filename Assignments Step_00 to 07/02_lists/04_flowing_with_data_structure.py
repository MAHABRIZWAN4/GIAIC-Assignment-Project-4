# In the information flow lesson, we discussed using a variable storing a number as an example of scope. We saw that changes we made to the number inside a function did not stay unless we returned it. This is true for what we call immutable data types which include things like numbers and strings.




print("Step 02_lists ==> 04_flowing_with_data_structure")

def add_three_copies(list,data):

      list.append(data)
      list.append(data)
      list.append(data)

    # user se message lo
user_message = input("\033[1;3mEnter the message to copy three times:\033[0m ") 



# khaali list banao
list_before = []

print("List before:", list_before)

# function call karo
add_three_copies(list_before, user_message)


print("List after:", list_before)



