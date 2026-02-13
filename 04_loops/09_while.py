# addition substraction until i exit it manually 

while True:
    print("============ Menu ============")
    print("1. Addition \n 2.Substraction \n 3.Exit")
   
    choice=int(input("Enter choice of Operatiion : "))

    if choice==1:
        a=int(input("Enter first number : "))
        b=int(input("Enter second number : "))
        print("Addition is : ",a+b)

    elif choice==2:
        a=int(input("Enter first number : "))
        b=int(input("Enter second number : "))
        print("Subtraction is : ",a-b)
    
    elif choice==3:
        print("Thank You For Attempting our Program!!")
        break

    else:
        print("Invalid choice ")