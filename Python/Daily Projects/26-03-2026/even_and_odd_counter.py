n = int(input("Enter a number: "))

even_counter = 0
odd_counter = 0

for i in range(1,n+1):
    if i % 2 == 0:
        even_counter += 1
    else:
        odd_counter += 1

print("Number of Even Numbers: ",even_counter)
print("Number of Odd Numbers: ",odd_counter)
