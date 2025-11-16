# program to store student names and their marks using a dictionary and print the student with the highest marks

#  first make an empty dictionary
students = {}

# asksing the number of students
n = int(input("Enter number of students: "))

# taking the input for names and marks
for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

# finding student with the highest marks
highest_student = max(students, key=students.get)

# The result is printed in the last step
print("\nStudent with the highest marks:")
print(highest_student, "got", students[highest_student], "marks")

