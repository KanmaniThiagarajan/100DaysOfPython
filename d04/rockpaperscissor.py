import random
rock='''   
                _
               | |
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   <
|_|  \___/ \___|_|\_\ 
'''

paper=''' 
_ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|  
'''

scissor='''  
  _       ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\.

                                   
                                   '''
game_images=[rock,paper,scissor] #list of images

your_choice=int(input("what do you choose? Type 0 for rock, 1 for paper or 2 for scissors. \n")) #users input
print(game_images[your_choice])
computer_choice=random.randint(0,2) #computers input
print("Computer chose: ")
print(game_images[computer_choice])
if your_choice==computer_choice:
    print("Its a draw")
elif your_choice==0: #o is rock
    if computer_choice==1: #1 is paper ( paper covers rock hence you win)
        print("Computer wins , paper covers rock")
    else:
        print("You Win, rock crushes scissor")
elif your_choice==1: #1 is paper
    if computer_choice==0: #1 is rock ( paper covers rock hence Computer wins)
        print("You win, paper covers rock")
    else:
        print("Computer wins , scissor cuts paper")
elif your_choice==2: #2 is scissor
    if computer_choice==0: #0 is rock ( rock crushes scissor hence You win)
        print("Computer wins , rock crushes scissor")
    else: #1 is paper ( scissor cuts paper)
        print("You win , scissor cuts paper")
else:
    print(f"You chose {your_choice} & Computer chose {computer_choice}, You lose")



