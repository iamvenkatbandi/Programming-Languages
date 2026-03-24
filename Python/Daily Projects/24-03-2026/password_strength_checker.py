password = input("Enter Password: ")

if len(password) > 8:
    strength = "Strong"
else:
    strength = "Weak"

print("Password Strength =",strength)
