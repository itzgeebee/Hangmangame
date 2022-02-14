# The paddle class which defines the attributes and methods of the paddle
from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.goto(position)

    def up(self):
        """moves the paddle in the north direction"""
        new_y = (self.ycor() + 20)
        self.goto(self.xcor(), new_y)

    def down(self):
        """moves the paddle in the south direction"""
        new_y = (self.ycor() - 20)
        self.goto(self.xcor(), new_y)
