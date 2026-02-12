# game level calculator 

score=int(input("Enter your Game Score : "))

if score>=1000:
    print("Level 3 is unlocked !!!")
elif score >=500:
    print("Level 2 is unlocked !!! ")
elif score>=100:
    print("Level 1 is unlocked !! ")
else:
    print("Keep playing to unlock all the levels !!!")