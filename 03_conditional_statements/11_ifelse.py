# login -- email id and phone number is required 

email=input("Enter Email ID : ")
mobno=int(input("Enter Mobile Number : "))

if email!="" and mobno!="":
    print("Login Successful !!!")
else:
    print("Please enter all credentials ! ")


#identify whether it is a weekday or it is weekend 

day=input("Enter Day name : ")

if day=="Saturday" or day=="Sunday":
    print("It is a WEEEKEND!!!! ")
else:
    print("It is a WEEKDAAY!!!! ")


# check the role and grant the access of system 

role=input("Enter ROle : ")

if role=="admin" or role=="manager":
    print("Full System Access - Admin and MAnager only ")
else:
    print("Access denied ! Need Admin or manager role to access the system ")