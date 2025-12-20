text = input("Enter a string:")
space_Count = sum([1 for ch in text if ch == ' '])
print("Number of Spaces:",space_Count)