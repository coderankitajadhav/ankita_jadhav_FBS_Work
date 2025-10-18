correct_userid = "admin"
correct_password = "1234"

userid = input("Enter user ID: ")
password = input("Enter password: ")


if userid == correct_userid and password == correct_password:
    print("Login successful!")
else:
    print("Login failed.")
