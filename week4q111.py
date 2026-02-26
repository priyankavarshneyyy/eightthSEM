# Dictionary of students and marks
students_marks = {
    "Amit": 82,
    "Riya": 74,
    "Sonal": 91,
    "Vikram": 68,
    "Neha": 78
}

# Display students scoring above 75
print("Students scoring above 75:")

for name, marks in students_marks.items():
    if marks > 75:
        print(name, "-", marks)
