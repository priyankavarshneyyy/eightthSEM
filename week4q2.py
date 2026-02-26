# Function to check palindrome
def is_palindrome(text):
    # Remove spaces and convert to lowercase
    text = text.replace(" ", "").lower()
    
    # Check if string is equal to its reverse
    if text == text[::-1]:
        return True
    else:
        return False


# Taking input from user
string = input("Enter a string: ")

# Calling the function
if is_palindrome(string):
    print("The string is a Palindrome.")
else:
    print("The string is not a Palindrome.")
