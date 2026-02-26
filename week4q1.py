# Program to find sum and average of user-given list

# Taking input from the user
numbers = list(map(float, input("Enter numbers separated by space: ").split()))

# Calculating sum
total = sum(numbers)

# Calculating average
average = total / len(numbers)

# Displaying results
print("List of numbers:", numbers)
print("Sum of the numbers:", total)
print("Average of the numbers:", average)
