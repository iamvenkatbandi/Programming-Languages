item1 = input("Enter Item Name: ")
price1 = float(input("Enter Price: "))
quantity1 = int(input("Enter the Quantity: "))
total1 = price1 * quantity1

item2 = input("Enter Item Name: ")
price2 = float(input("Enter Price: "))
quantity2 = int(input("Enter the Quantity: "))
total2 = price2 * quantity2

item3 = input("Enter Item Name: ")
price3 = float(input("Enter Price: "))
quantity3 = int(input("Enter the Quantity: "))
total3 = price3 * quantity3

final_bill = total1 + total2 + total3

print("\n--- BILL ---")
print(item1, "=", price1)
print(item2, "=", price2)
print(item3, "=", price3)
print("Total Amount to Pay: ",final_bill)

