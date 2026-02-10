#check the balance and accordingly i need to withdraw the money and limit = 2000

balance=float(input("Enter Balance : "))
amount=float(input("Enter amount to withdraw (max limit : 2000 /-) : "))

print("Balance is : ",balance)

if amount<=balance and amount<=2000:
    balance-=amount
    print("Withdrawed Amount Successfully !!!")
    print("Balance is : ",balance)
else:
    print(" Faile to Withdrawed Amount !!!")


