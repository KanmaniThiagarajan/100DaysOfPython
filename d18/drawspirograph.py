import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fast")


def randomcolor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_color = (r, g, b)
    # Tuple - its just like a list but within round brackets, and it can not be changed once created
    # list can be changed but a tuple cannot
    return my_color


incrementAngle = 10
angle = 0
for i in range(int(360/incrementAngle)):
    tim.setheading(angle)
    tim.color(randomcolor())
    tim.circle(100)
    angle += incrementAngle

my_screen = t.Screen()
my_screen.exitonclick()