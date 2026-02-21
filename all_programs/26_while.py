while True:
    print("=========== Menu =========")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice=int(input("Enter Choice :: "))
    if choice==5:
        break

    a=int(input("Enter First Number : "))
    b=int(input("Enter Second Number : "))

    if choice==1:
        print("Result is :: ",a+b)
    elif choice==2:
        print("Result is :: ",a-b)
    elif choice==3:
        print("Result is :: ",a*b)
    elif choice==4:
        if b!=0:
            print("Result is :: ",a/b)
        else:
            print("Cannot Divide By 0 ")




