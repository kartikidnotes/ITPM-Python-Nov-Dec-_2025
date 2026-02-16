num=int(input("Enter Number :: "))
digits=0
even=0
odd=0

while num>0:
    d=num%10
    digits=digits+1

    if d%2==0:
        even=even+1
    else:
        odd=odd+1

    num//=10

print("Total DIgits :: ",digits)
print("Even Digits : ",even)
print("Odd Digits : : ",odd)



# choice == 
# 1. find square
# 2.cube of number
# 3.even /odd
# 4.factorial
# 5. exit