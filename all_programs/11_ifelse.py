# take salary from user sal<5000 bonus --apply (2000)

salary=float(input("Enter Salary :: "))

if salary<5000:
    total_sal=salary+2000
    print("Bonus Addded ")
    print("Total Salary :  ",total_sal)
else:
    print("Not Eligible for Bonus ")


#atm Withdraw
balance=10000

amt=float(input("Enter Amount To Withdraw :: "))

if amt<balance:
    rbalance=balance-amt
    print("Amount Withdraw Successfully !!")
    print("Balance is :: ",rbalance)
else:
    print("Insufficient Balance !!")
