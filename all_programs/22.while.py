# ATM System

balance=10000

while True:
    print("========== Menu ==========")
    print("1. Check Balance")
    print("2. Deposit Amount")
    print("3. Withdraw")
    print("4. Exit")

    choice=int(input("Enter Choice From above Options :: "))

    if choice==1:
        print("Balance is :: ",balance)
    elif choice==2:
        amt=int(input("Enter AMount To Deposit ::"))
        balance=balance+amt
        print("Balance is :: ",balance)
    elif choice==3:
        amt=int(input("Enter AMount To Withdraw ::"))
        if amt<=balance:
            balance=balance-amt
            print("Balance is :: ",balance)
        else:
            print("Insufficient Balance !!")

    elif choice==4:
        print("Thank YOu !!!")
        break
    else:
        print("Invalid Choice ")



