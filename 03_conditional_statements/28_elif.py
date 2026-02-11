#calculate bonus based on experience 
# 5+ ---> 20%
# 3-5 ---> 10%
# 1-3 -->5%
# <1 --> No bonus 
# 

salary=float(input("Enter Salary : "))
exp=int(input("Enter Experience : "))

if exp>=5:
    bonus=salary*0.20
    total_sal=salary+bonus
    print("===="*10)
    print("Bonus is : ",bonus)
    print("Total Salary with Bonus : ",total_sal)
elif exp>=3 and exp<5:
    bonus=salary*0.10
    total_sal=salary+bonus
    print("===="*10)
    print("Bonus is : ",bonus)
    print("Total Salary with Bonus : ",total_sal)
elif exp>=1 and exp<3:
    bonus=salary*0.05
    total_sal=salary+bonus
    print("===="*10)
    print("Bonus is : ",bonus)
    print("Total Salary with Bonus : ",total_sal)
else:
    print("===="*10)
    print("Bonus is not Valid for less than 1 year ")



#create a simple calculator 
# if opr=="+"
# print("Adddition is : "a+b)


# age --> <18 -- child
    #   --> 18 - 60 -- adult 
    # ---> >60 --- senior citizen 


# accept the CTC from user
# CTC >7,0000 --->  15%
# CTC >5,0000 <7L --->  10%
# CTC >3,0000 <5L --->  5%
# CTC <3,0000 < 2L--->  2%


