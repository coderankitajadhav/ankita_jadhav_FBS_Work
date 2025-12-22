year = int(input("Enter year to check leap year or not: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("The given year is a leap year")
        else:
            print("This is not a leap year")
    else:
        print("The given year is a leap year")
else:
    print("This is not a leap year")