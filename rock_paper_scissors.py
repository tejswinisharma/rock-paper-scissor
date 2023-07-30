import random
user_wins =0
computer_wins =0
options=["rock","paper","scissor"]

while True:
    user_inputs = input("type rock/ paper/ scissor or Q to quit: ").lower()
    if user_inputs =='q':
        quit()
        break
    if user_inputs  not in options :
        continue
    random_number= random.randint(0,2)
    computer_pick = options[random_number]
    print("computer picked",computer_pick+".")

    if user_inputs== "rock" and computer_pick=="scissor":
        print("you win")
        user_wins+=1
    elif user_inputs== "paper" and computer_pick=="rock":
        print("you win")
        user_wins+=1
    elif user_inputs== "scissor" and computer_pick=="paper":
        print("you win")
        user_wins+=1
    else:
        print("you lose")
        computer_wins+=1
print("you win",user_wins,"times")
print("computer win",computer_wins,"times")
print("goodbye!")
