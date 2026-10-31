# Snake Water and Gun game 

import random
'''
1 for snake 
-1 for water 
0 for gun
'''
computer = random.choice([1, -1, 0])
YourChoice = input("Enter your choice :")
YouDict = {"s": 1, "w": -1, "g": 0}
ReverseDict = {1: "snake", -1: "water", 0: "gun"}

You = YouDict[YourChoice]

print(f"You chose {ReverseDict[You]}\nComputer chose {ReverseDict[computer]}")

if(computer == You):
    print("Its a Draw")

else:
    if(computer == -1 and You == 1):
        print("You win!")

    elif(computer == 1 and You == 0):
        print("You Lose!")

    elif(computer == 1 and You == 1):
        print("You Lose!")

    elif(computer == 0 and You == -1):
        print("You win!")

    elif(computer == 0 and You == 1):
        print("You Lose!")

    else:
        print("Something went wrong")
    