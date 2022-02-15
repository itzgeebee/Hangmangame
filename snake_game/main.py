# import the needed packages
from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard

# create the screen object and set the attributes
screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# set all the buttons to move the snake in different directions
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

# set condition for the program to run
game_on = True
while game_on:
    x = 0.1
    screen.update()
    time.sleep(x)
    snake.move()


    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        scoreboard.update_scoreboard()
        snake.extend()

    # detect collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        scoreboard.reset()
        snake.reset_snake()


    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset_snake()





screen.exitonclick()
