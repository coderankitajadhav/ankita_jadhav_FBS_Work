

n = int(input("Enter number of terms: "))
total = 0
term = 1

for _ in range(n):
    total += term
    term *= 2

print("Sum of the series =", total)
