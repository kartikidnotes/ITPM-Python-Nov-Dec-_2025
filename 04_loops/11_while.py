# ATM System

balance=int(input("Enter Balance ::  "))

while True:
    print("=========== Menu =========")
    print("1. Check Balance ")
    print("2. Deposit ")
    print("3. Withdraw ")
    print("4. Exit ")

    choice=int(input("Enter Choice from above options :: "))

    if choice==1:
        print("Your Balance is :: ",balance)
    
    elif choice==2:
        amount=int(input("Enter Amount to Depoist :: "))
        balance=balance+amount
        print("Your Balance is :: ",balance)

    
    elif choice==3:
        amount=int(input("Enter Amount to Withdraw :: "))
        if amount<=balance:
            balance=balance-amount
            print("Your Balance is :: ",balance)

        else:
            print("Insufficient Balance !!! ")
    elif choice==4:
        pint("Thank You For Using ATM !!! ")
        break
    else:
        print("Invalid Choice ")



    