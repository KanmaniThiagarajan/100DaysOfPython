#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

#Function to generate a random number 
def generate_number():
    number = int(random.choice((range(1,101))))
    return number

#Function to check the number guessed by user matches with computer
def level(attempts):
    #attempts = 5
    user_won = False
    while attempts > 0:
        print (f"You have {attempts} attempts")
        user_guess= int(input("Make a guess : "))
        print(f"User Guess is {user_guess}")
        if user_guess > result: 
            print("Too High")
            attempts -= 1
        elif user_guess < result:
            print("Too low")
            attempts -= 1
        elif user_guess == result:
            attempts = 0
            user_won = True
    if user_won:
        print("You guessed it correctly You won")
    else:
        print("You guessed an incorrect number . You Lose")

#Function to set the no of attempts based on difficulty level and call "level" function with input parameter as no of attempts
def guess_number():
    if difficulty == "Easy":
        attempts = 10
        level(attempts)
    elif difficulty == "Hard":
        attempts = 5
        level(attempts)

        
import random
print("Welcome to the number guessing game")
print("I am thinking a number between 1 and 100")
difficulty = input("Choose a Difficulty . Easy or Hard: ")
result = generate_number()
guess_number()