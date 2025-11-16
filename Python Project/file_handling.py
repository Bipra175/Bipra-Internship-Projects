# program to save user data in a text file and show all the saved entries

# to open the file in append mode to add new data
with open("userdata.txt", "a") as f:
    name = input("Enter name: ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")
    f.write(f"Name: {name}, Email: {email}, Phone: {phone}\n")

print("\nAll saved entries:\n")

# to open file in read mode to show data
with open("userdata.txt", "r") as f:
    print(f.read())
