from art import logo
from art import vs
from game_data import data
from replit import clear
import random

#function to compare the followers count of two list
def compareList(list_1, list_2):
    return list_1['follower_count'] > list_2['follower_count']
#generating two list to compare
compare_a = random.choice(data)
compare_b = random.choice(data)
print(logo) #print higher lower logo
score = 0
should_end = False #loop to continue until its true
while not should_end:
    
    compare_a = compare_b #if the user guesses correctly, then b becomes a
    compare_b = random.choice(data)
    print(
    f"Compare A: {compare_a['name']} , {compare_a['description']}, {compare_a['country']}"
)
    print(vs)
    print(
        f"Against B: {compare_b['name']} , {compare_b['description']}, {compare_b['country']}"
    )

    user_choice = input("Who has more followers A or B: ").lower()
    is_A_correct = compareList(compare_a, compare_b)
    is_B_correct = compareList(compare_b, compare_a)
    clear()
    print(logo)
    if user_choice == 'a':
        if is_A_correct:
            score += 1
            print(f"You are right.  Your current score is {score}")
        else:
            print(f"Sorry ! That is wrong. Your final score is {score}")
            should_end = True
    elif user_choice == 'b':
        if is_B_correct:
            score += 1
            print(f"You are right.  Your current score is {score}")
        else:
            print(f"Sorry ! That is wrong. Your final score is {score}")
            should_end = True
