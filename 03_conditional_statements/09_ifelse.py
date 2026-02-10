#check the username and password must be compulsary this :
# username= admin and password="admin@12345"


username=input("Enter Username : ")
password=input("enter Password : ")

if username=='admin' and password=='admin@12345':
    print("Login Successful!!!")
else:
    print("Invalid Credentials ")