# A two player pong game created with the python turtle package


# import all required classes and packages
from turtle import Turtle, Screen
from paddle import Paddle
import time
from ball import Ball
from score_board import ScoreBoard

# initialize the screen attributes
screen = Screen()
screen.setup(width=900, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# create the objects (paddles, ball, scoreboard)
l_paddle = Paddle((-430, 0))
r_paddle = Paddle((430, 0))
ball = Ball()
scoreboard = ScoreBoard()



screen.listen()
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")

screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="x")



def restart():
    """takes no arguments. starts game when called"""
    # condition for running the game
    game_on = True
    while game_on:

        screen.update()
        time.sleep(ball.gamespeed)
        ball.move_around()
        x = ball.xcor()
        y = ball.ycor()

        # detect collision with top wall
        if y > 280 or y < -280:
            ball.bounce_wall()

        # detect collision with pad
        if ball.distance(r_paddle) < 40 and ball.xcor() > 420 or ball.distance(l_paddle) < 40 and ball.xcor() < -420:
            ball.bounce_paddle()


        # right side miss
        if ball.xcor() > 430:
            ball.reset_position()
            scoreboard.increase_lscore()


        # left side miss
        if ball.xcor() < -430:
            ball.reset_position()
            scoreboard.increase_rscore()

        # condition for game termination
        if scoreboard.left_score > 11 or scoreboard.right_score > 11:
            game_on = False
            scoreboard.game_over()


restart()









screen.exitonclick()
