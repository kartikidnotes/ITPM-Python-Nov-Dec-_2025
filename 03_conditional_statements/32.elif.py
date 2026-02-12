#courier charges 

weight=float(input("Enter the Courier Weight (in kg) : "))

if weight<=1:
    print("Charges is : 50 /- ")
elif weight<=5:
    print("Charges is : 80 /- ")
elif weight<=10:
    print("Charges is :200 /- ")
else:
    print("Charges is 500 /- ")
