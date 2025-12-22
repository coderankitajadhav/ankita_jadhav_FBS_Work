num = int(input("Enter a 3-digit number: "))


first = num // 100
second = (num // 10) % 10
third = num % 10

# Check the condition
if first == 2 * second and first * 2 == third:
    print("Yes, you have done it")
else:
    print("Please try next time")