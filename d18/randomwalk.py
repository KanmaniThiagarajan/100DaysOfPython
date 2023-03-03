from turtle import Turtle, Screen
import random

turtle = Turtle()

directions = [0, 90, 180, 270]
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
turtle.pensize(5)
turtle.speed("fastest")


def randomwalk():
    for i in range(200):
        color = random.choice(colours)
        direction = random.choice(directions)
        turtle.color(color)
        turtle.forward(30)
        turtle.setheading(direction)


randomwalk()

my_screen = Screen()
my_screen.exitonclick()
