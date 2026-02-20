#give atm menu card

choice=int(input("Enter Choice : /n1. Deposit /n2.Withdraw \n3.Check Balance  :: "))

if choice==1:
    print("Deposit Option is selected ")
elif choice==2:
    print("Withdraw Option is selected ")
elif choice==3:
    print("Check Balance Option is selected ")
else:
    print("Invalid Option is selected ")


