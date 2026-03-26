correct_password = "admin1234"

for i in range(3):
    password = input("Enter a Password: ")
    
    if password == correct_password:
        print("Access Granted!")
        break
    else:
        print("Wrong Password!")

else:
    print()
    print("Account Locked!")
