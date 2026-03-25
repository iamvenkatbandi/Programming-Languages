while True:
    number = int(input("Enter Number to Generate Multiplication Table: "))

    for i in range(1,11):
            print(number,"X",i,"=",number*i)
    
    option = input("Do you want to Continue (yes/no): ")

    if option == "no":
        print("Exiting.....")
        break
