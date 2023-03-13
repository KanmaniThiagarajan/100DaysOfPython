from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"Score:{self.score} ", False, align=ALIGNMENT, font=FONT)
        # write function to show the title on the screen

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over ", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        # if the dot and segment[0] has a distance less than 10 score is incremented
        self.score += 1
        self.clear()
        # as the no of times the dots and head crossing increases score increases so wiping the previous score
        # using clear method
        self.update_score()
        # update score again everytime after score is increased by 1
