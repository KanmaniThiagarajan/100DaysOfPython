# changing the RGB colors in random walk using tuple
import random
import turtle

tim = turtle.Turtle()
turtle.colormode(255)
directions = [0, 90, 180, 270]
tim.pensize(5)
tim.speed("fastest")


def randomcolor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_color = (r, g, b)
    # Tuple - its just like a list but within round brackets, and it can not be changed once created
    # list can be changed but a tuple cannot
    return my_color


def randomwalk():
    for i in range(200):
        direction = random.choice(directions)
        tim.color(randomcolor())
        tim.forward(30)
        tim.setheading(direction)


randomwalk()

my_screen = turtle.Screen()
my_screen.exitonclick()
