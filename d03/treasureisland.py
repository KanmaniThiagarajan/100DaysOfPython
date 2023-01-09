print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|\n''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
left_or_right=input("You are at the junction , where do you want to go left or right? ").lower()
if left_or_right=="left":
    swim_or_wait=input("Do you want to wait for a boat or swim across the river? ").lower()
    if swim_or_wait=="wait":
        door=input("You have reached the entrance, which color door do you want to open Red or Blue or Yellow? ").lower()
        if door=="yellow":
            print("You have found the treasure !! You won :) !!")
        elif door=='red':
            print("You have opened the door to fire, Your game is over :(") 
        elif door=='blue':
            print("You have opened the door to monsters,Your game is over :(")       
        else:
            print("No Such Door. Your game is over :(!!!")
    else:
        print("You are eaten by the crocodiles , You cant cross the river now. Your game is over:(!!")  
else:
    print("Since You have turned right, you fell into a hole. Your game is over :(!!")                      


    
    
