# Input a 3-digit number as string to easily check digits
num = input("Enter a 3-digit number: ")

# Check if the number is a palindrome
if num == num[::-1]:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
