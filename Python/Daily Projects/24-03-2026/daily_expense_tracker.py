food = float(input("Enter the Food Expense = "))
travel = float(input("Enter the Travel Expense = "))
other = float(input("Enter the Other Expense = "))

total = food + travel + other

if food > travel and other:
    high = "Food"
elif travel > other and food:
    high = "Travel"
else:
    high = "Other"

print("\n---Daily Expenses---")
print("Total Expense = ",total)
print("Most Spent Category = ",high)
