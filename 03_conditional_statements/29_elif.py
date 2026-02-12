# check a temperature 
# temp >41 ==> hot
#     25 to 40 -- normal
#     10-25 ==> cold
# below 10 == extremely cold 


temp=int(input("Enter Temperature : "))

if temp>40:
    print("The Temperature is too hot !! ")
elif temp>=25 and temp<=40:
    print("Temprature is Normal !!! ")
elif temp>=10 and temp<25:
    print("Temperatur is Cold")
elif temp<10:
    print("Temperature is Extremely Cold ")
else :
    print("Invalid Input ")