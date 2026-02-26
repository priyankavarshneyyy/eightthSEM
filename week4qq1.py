# Create an empty dictionary
students_marks = {}

# Take number of students as input
n = int(input("Enter number of students: "))

# Input student name and marks
for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks of the student: "))
    students_marks[name] = marks

# Display students scoring above 75
print("\nStudents scoring above 75:")
for name, marks in students_marks.items():
    if marks > 75:
        print(name, "-", marks)
