# reverse a number


a=1234
rev=0

while a>0:
    digit=a%10
    rev=rev*10+digit
    a//=10

print("Reveerse number is : ",rev)