# Get marks for 5 subjects
s1 = float(input("Enter marks for Subject 1: "))
s2 = float(input("Enter marks for Subject 2: "))
s3 = float(input("Enter marks for Subject 3: "))
s4 = float(input("Enter marks for Subject 4: "))
s5 = float(input("Enter marks for Subject 5: "))

# Calculate total and percentage
total = s1 + s2 + s3 + s4 + s5
percentage = (total / 500) * 100

# Show result
print("Total Marks:", total)
print("Percentage:", percentage)
