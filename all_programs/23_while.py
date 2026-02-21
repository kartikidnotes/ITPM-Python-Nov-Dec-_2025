correct_password="admin@123"
attempt=0

while attempt<3:
    password=input("Enter Password :: ")
    
    if password==correct_password:
        print("Login Successfully Done !!!")
        break
    else:
        print("Wrong Password ")
        attempt+=1

if attempt==3:
        print("Account Blocked for 24 Hours !")