principal = int(input("Enter the Principal Amount: "))
rate = int(input("Enter the % of Interest: "))
time = int(input("Enter the Time Limit (In Years): "))

print()

for year in range(1,time+1):
    interest = (principal * rate * time)/100
    print("Year",year,": Interest = ",interest)

