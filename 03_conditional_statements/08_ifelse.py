# check the Validity of my recharge plan 

days=int(input("Enter Days : "))

if days>0:
    print("Active Recharge Plan !")
else:
    print("Expired Recharge Plan !")



# delivery charges
price=float(input("Enter Amount :" ))

if price>=500:
    print("Free Delivery !!!!! ")
else:
    print("Delivery Charges will be Applicable ! ")
