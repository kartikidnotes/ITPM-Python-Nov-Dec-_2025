# password attempt -  3 max

attempt=1

while attempt<=3:
    pwd=input("Enter Password : ")
    if pwd=="admin@1234":
        print("Login Successfull!!")
        break
    else:
        print("Invalid Input ")
    attempt+=1

