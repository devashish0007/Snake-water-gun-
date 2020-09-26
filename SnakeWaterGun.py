# Snake water gun
import random

def not_valid(string):
    if(str(string)):
        string = string.capitalize()
        if(string=="Snake" or string=="Gun" or string=="Water"):
            return False
        else:
            return True

    else:
        return True

def check(computer,player):
    if(computer==1):
        if( player==1):
            print("\t Result : Draw")
            return "draw"
        elif(player==2):
            print("\t Result : you loose")
            return "computer"
        else:
            print(" \tResult : you won")
            return "player"
    elif(computer==2):
        if (player == 1):
            print("\t Result : you won")
            return "player"
        elif (player == 2):
            print("\t Result : Draw")
            return "draw"
        else:
            print(" \tResult : you loose")
            return "computer"
    else:
        if (player == 1):
            print(" \tResult : you loose")
            return "computer"
        elif (player == 2):
            print("you won")
            return " \tResult : player"
        else:
            print(" \tResult : Draw")
            return "draw"


move = {"Snake":1, "Water":2, "Gun":3}
randommove = ["Snake", "Water", "Gun"]
i=1
computer = 0
player = 0
draw = 0
while i<=10:
    computer_choice = random.choice(randommove)
    player_choice = input(f"\nRound {i} Choose from Snake/Water/Gun : ")
    if not_valid(player_choice):
        print(f"\n*********************************** Rounds Left : {10-i+1} ****************************************")
        print("Wrong Input Please re-enter your choice -")
        continue
    player_choice =player_choice.capitalize()
    print(f"Your Choice : Computer Choice\n\t\t{player_choice}\t:\t{computer_choice}")
    result = check(move[computer_choice],move[player_choice])
    print(f"\n*********************************** Rounds Left : {10-i} ****************************************")
    if result=="player":
        player +=1
    elif result=="computer":
        computer +=1
    else:
        draw +=1
    i +=1


print(f"Scores :\n\tPlayer Score : {player}\n\tComputer Score : {computer}\n\tDraw Matches : {draw}\n")
if(computer > player):
    print("\tYou lose!")
elif(computer<player):
    print("\tyou Won!")
else:
    print("\tMatch Draw")



