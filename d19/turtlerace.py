# turtle race between multiple turtles
# different colors for different turtles and names as well
# Pop to make your bet on who will win the race and enter the input and color is chosen
# line all the turtle
# Turtles will take random steps towards the right end of the screen
# one who reaches first is the winner
# print the winner name and compare with your bet
# Print whether you lose or won

from turtle import Turtle, Screen
import random

# Created multiple turtles as object from same Turtle() class
screen = Screen()


screen.setup(width=700, height=600)
colors = ["red", "blue", "green", "orange", "purple", "brown"]

is_race_on = False
user_guess = screen.textinput(title="Turtle race", prompt="make your bet. enter the color")
y = [-70, -40, -10, 20, 50, 80]
all_turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle()
    new_turtle.color(colors[turtle_index])
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.goto(0, y[turtle_index])
    all_turtles.append(new_turtle)

if user_guess:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        distance = random.randint(20, 30)
        turtle.forward(distance)
        # print(f"Turtle {turtle.pencolor()} is jumping {distance}. Total distance travelled: {turtle.xcor()}")

        if turtle.xcor() > 50 and is_race_on :
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_guess == winning_color:
                print(f"You won..Winner is {winning_color} turtle")
            else:
                print(f"You lose.. Winner is {winning_color} turtle")


screen.exitonclick()