# check login


username=input("Enter username : ")
password=input("Enter Password : ")

status="Login Successful" if username=="admin" and password=="admin@12345" else "Login Failed"

print(status)


#num positive 
num=int(input("Enter number : "))

res="Positive number " if num>0 else "Negative" if num<0 else "Number is equal to 0"

print(res)