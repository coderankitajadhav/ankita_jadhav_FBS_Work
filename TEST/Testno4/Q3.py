n = 10

# Top horizontal line
print("*" * 22)

# Diagonal stars
for i in range(n):
    print(" " * (20 - i * 2) + "*")

# Bottom horizontal line with last star
print("*" * 21 + " *")