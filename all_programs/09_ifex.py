#maximum from two number 
n1=int(input("Enter First Number :: "))
n2=int(input("Enter Second Number :: "))

if n1>n2:
    print("Number 1 is greater than Number 2")

if n2>n1:
    print("Number 2 is greater than Number 1")


#voting system
age=int(input("Enter Age :: "))

if age>=18:
    print("Eligible For Voting ")
if age<18:
    print("NOT Eligible For Voting ")
