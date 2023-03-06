import turtle as t

tim = t.Turtle()
screen = t.Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


# def move_counter_clockwise():
#     tim.left(10)
#
#
# def move_clockwise():
#     tim.right(10)


def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()

#onkey function when you press the key = "w", the function is called 
#to use onkey screen.listen() should be used