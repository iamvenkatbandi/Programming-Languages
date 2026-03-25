correct_username = "admin"
correct_password = "1234"

for i in range(3):
    username = input("Enter Username: ")
    password = input("Enter Password: ")
        
    if username == correct_username and password == correct_password:
        print("Login Successful!")
        break
    else:
        print("Invalid Credentials!")
        print("\n")

    if i == 2:
        print("No attempts left!")

