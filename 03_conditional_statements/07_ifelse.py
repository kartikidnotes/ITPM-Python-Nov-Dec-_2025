# check maximum number without using inbuilt function : not using min and max ())
num1=int(input("Enter first number : "))
num2=int(input("Enter second number : "))

#maximum
if num1>num2:
    print(num1 , " is greater than " ,num2)
else:
    print(num2 , " is greater than " ,num1)

#minimum
if num1<num2:
    print(num1 , " is minimum than " ,num2)
else:
    print(num2 , " is minimum than " ,num1)