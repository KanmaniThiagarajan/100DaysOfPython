# Requirement :
# 1. Create a snake body
# 2. Move the snake
# 3.control the snake
# 4. Detect collision with food
# 5. Create a scoreboard
# 6. Detect wall collision ( game over)
# 7. Detect tail collision ( game over)

# Create Snake Body
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600) #set the width and height of the screen
screen.bgcolor("black")
screen.title("SnakeGame")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# control snake on key press

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # make the snake move
    snake.snake_move()

    # detect food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()

    # detect wall collision
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # detect tail collision
    # head (Segment[0]) collides with any other segment ( segment range(1,len(segment))
    # game over
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
