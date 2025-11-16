# program to print multiplication table for a number (1 to 10)
# Asking the user for a number
num = int(input("Enter a number: "))

# checking if number is between 1 and 10
if 1 <= num <= 10:
# printing the table using a loop
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)
else:
    print("Enter any number between 1 and 10")

