# random number 

import random

secretnumber=random.randint(1,100)
attemp=0
max_attempt=5


while attemp<max_attempt:
    guess=int(input("Enter the number : (1-100) :: "))
    attemp+=1

    if guess==secretnumber:
        print("Correct !!! You WON !!!")
        break
    elif guess<secretnumber:
        print("Too LOW!!")
    else:
        print("Too HIGH!!")

if guess!=secretnumber:
    print("Game Over !!!! The number was :: ",secretnumber)