# # create a bill calculator

# unit :
# 0-100 ---> 3 rs per unit
# 101-200 ---> 5 rs per unit
# 201-300 ---> 7 rs per unit
# > 300 ---> 10 rs per unit

units=float(input("Enter the units : "))

if units<=100:
    bill=units*3
    print("==="*10)
    print("Consumed Units is : ",units)
    print("The bill is : ",bill)
elif units>100 and units<=200:
    print("==="*10)
    print("Consumed Units is : ",units)
    bill=units*5
    print("The bill is : ",bill)
elif units>200 and units<=300:
    print("==="*10)
    print("Consumed Units is : ",units)
    bill=units*7
    print("The bill is : ",bill)
else:
    print("==="*10)
    print("Consumed Units is : ",units)
    bill=units*10
    print("The bill is : ",bill)