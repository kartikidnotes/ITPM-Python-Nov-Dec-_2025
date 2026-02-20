s1=float(input("Enter Subject 1 marks : "))
s2=float(input("Enter Subject 2 marks : "))
s3=float(input("Enter Subject 3 marks : "))


per=(s1+s2+s3)/3
print("Percentage is :: ",per)

if per>=90:
    print("Grade A")
elif per<90 and per>=75:
    print("Grade B")
elif per<75 and per>=50:
    print("Grade C")
elif per<50 and per>=35:
    print("Grade D")
else:
    print("Fail")