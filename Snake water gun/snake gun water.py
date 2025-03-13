import random
print(" 1.snake \n 2.water \n 3.gun")
character = int(input("Enter Number to select and win :"))
if (character not in range(1,4)):
    print("Enter a valid Number")

l=[1,2,3]
computer = random.choice(l)
print("compter :",computer)
print("player :",character)

if (computer == 1) and (character==2):
    print("Player Wins")
elif (computer == 2) and (character==3):
    print("Player Wins")

elif (computer == 3) and (character==1):
    print("Player Wins")

elif (computer == character):
    print("Player Draw")
else:
    print("Computer Wins")