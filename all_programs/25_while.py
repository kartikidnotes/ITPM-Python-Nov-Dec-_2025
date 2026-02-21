# Bank Loan 

while True:
    salary=float(input("Enter Salary [0 For Exit ] :: "))
    if salary==0:
        break

    if salary>=25000:
        print("Eligible for Loan ")
    else:
        print("NOT Eligible for Loan ")

