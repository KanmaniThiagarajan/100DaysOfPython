# import colorgram
# from colorgram import Color
#
# # Extract 6 colors from an image.
# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
color_list = [(226, 229, 235), (244, 237, 222), (243, 234, 240), (232, 242, 237), (192, 165, 115), (138, 166, 190),
              (56, 102, 140), (141, 91, 50), (12, 23, 55), (222, 207, 123), (182, 154, 42), (61, 22, 11),
              (182, 146, 165), (142, 177, 151), (72, 117, 81), (58, 15, 26), (126, 79, 102), (130, 30, 16),
              (15, 39, 23), (24, 53, 127), (177, 188, 215), (164, 104, 134), (115, 31, 46), (97, 150, 100),
              (98, 121, 172), (210, 178, 197), (174, 105, 93), (74, 150, 165), (25, 91, 65), (172, 205, 180)]


def draw_dot():
    for i in range(10):
        color = random.choice(color_list)
        tim.hideturtle()
        tim.dot(10, color)
        tim.penup()
        tim.forward(20)


def draw_spot_paint():
    for i in range(10):
        draw_dot()
        tim.setposition(0, tim.position()[1]+20)


draw_spot_paint()

my_screen = t.Screen()
my_screen.exitonclick()
