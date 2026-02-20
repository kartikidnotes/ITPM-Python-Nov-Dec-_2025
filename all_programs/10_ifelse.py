age=int(input("Enter Age :: "))

if age>=18:
    print("Eligible For Voting ")
else:
    print("NOT Eligible For Voting ")


#check password == admin@1234
password=input("Enter Password :: ")
if password=="admin@1234":
    print("Correct Password !! ")
else:
    print("InCorrect Password !! ")

#check num -- 3 and 7 divisbility check 
# eg : 21 -- 3 and 7

num=int(input("Enter Number :: "))
if num%3==0 and num%7==0:
    print("Number is divisible by 3 and 7 both")
else:
    print("Number is divisible NOT by 3 and 7 both")

