# password length

while True:
    password=input("Enter Password :: ")
    if len(password)<8:
        print("Not a Strong Password : Short PAssword ")
    else:
        print("PAssword Set Successfully ")
        break