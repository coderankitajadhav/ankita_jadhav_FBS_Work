text = input("Enter a string:")
result = ''.join([ch for ch in text if ch.lower() not in 'aeiou'])
print("Without Vowels",result)