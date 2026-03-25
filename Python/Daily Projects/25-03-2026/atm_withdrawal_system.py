account_balance = float(input("Enter Your Account Balance: "))
withdrawal_amount = float(input("Enter the Amount You want to Withdraw: "))

if withdrawal_amount > account_balance:
    print("Insufficient Balance!")
else:
    new_account_balance = account_balance - withdrawal_amount
    print("Amount Withdrawn!")


print("\n---Options to Consider---")
print("1. View Account Balance")
print("2. Exit")

option = int(input("Choose the Option: "))

if option == 1:
    print("Checking Balance.....")
    print("Account Balance: Rs.",new_account_balance)
    print("Thank you for Using BVC Bank. Visit Again!")
elif option == 2:
    print("Exiting.....")
    print("Thank You for Using BVC Bank. Visit Again!")
