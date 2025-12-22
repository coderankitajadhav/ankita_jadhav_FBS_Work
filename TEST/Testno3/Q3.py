num = int(input("How many employees? "))

for i in range(num):
    print("\nEmployee", i + 1)
    basic_salary = int(input("Enter basic salary: "))

    DA = 10/100 * basic_salary
    TA = 12/100 * basic_salary
    HRA = 15/100 * basic_salary

    total_salary = basic_salary + DA + TA + HRA

    print("Total salary of employee", i + 1, "is:", total_salary)
