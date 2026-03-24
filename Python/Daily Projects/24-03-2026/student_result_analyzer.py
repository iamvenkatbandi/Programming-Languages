sub1 = int(input("Enter Subject 1 Marks: "))
sub2 = int(input("Enter Subject 2 Marks: "))
sub3 = int(input("Enter Subject 3 Marks: "))
sub4 = int(input("Enter Subject 4 Marks: "))
sub5 = int(input("Enter Subject 5 Marks: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
average = total/5

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "Fail"

print("\n---Result---")
print("Total =",total)
print("Average =", average)
print("Grade =", grade)
