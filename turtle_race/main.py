# A simple turtle racing game made with the turtle package
import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=900, height=600)
user_bet = screen.textinput(title="make your bets", prompt="Which turtle will win? pick a colour: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []


def make_turtle(new_turtle, num_of_turtles, colour):
    """takes in 3 arguments and makes new turtles from the 'colors' list and appends them to a new list 'all turtles'
    """
    # loop through the specified range and make new turtles with the description
    for i in new_turtle:
        col = Turtle("turtle")
        col.penup()
        col.color(colors[i])
        col.goto(-440, (num_of_turtles))
        num_of_turtles -= 60
        all_turtles.append(col)


make_turtle(range(6), 180, colors)

# condition for running
if user_bet:
    is_race_on = True
while is_race_on:

    # condition for terminating the program
    for turts in all_turtles:
        if turts.xcor() > 420:
            is_race_on = False
            winner = turts.pencolor()
            if winner == user_bet:
                print(f"You win {winner}")
            else:
                print(f"You lost, {winner} is the winner ")
        else:
            random_distance = random.randint(0, 10)
            turts.forward(random_distance)

screen.exitonclick()
