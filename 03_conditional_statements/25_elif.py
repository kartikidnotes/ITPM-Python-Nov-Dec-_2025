# design a marksheet

m1=float(input("Enter Subject 1 marks : "))
m2=float(input("Enter Subject 2 marks : "))
m3=float(input("Enter Subject 3 marks : "))

total=m1+m2+m3
per=total/3
print("Percentage is : ",per)

if per<=100 and per>85:
    print("Grade A ")
elif per<=85 and per>70:
    print("Grade B ")
elif per<=70 and per>35:
    print("Grade C ")
else:
    print("Fail ")