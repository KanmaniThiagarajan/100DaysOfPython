from turtle import Turtle, Screen
from drawshapesdata import data
from drawshape import *

timmy = Turtle()

for i in data:
    shape = i["shape"]
    sides = i["sides"]
    color = i["color"]
    drawShape = DrawShape(shape, sides, color)
    drawShape.draw(timmy)

my_screen = Screen()
my_screen.exitonclick()
