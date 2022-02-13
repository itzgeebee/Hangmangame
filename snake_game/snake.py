# import turtle
from turtle import Turtle

# define all the constant variables
START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# create the snake class
class Snake:

    def __init__(self):
        """ contructs the snake objects and initializes the attributes"""

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.shape("turtle")


    def create_snake(self):
        """ takes no arguments. creates and defines all the attributes for the initial snake"""
        for i in START_POSITION:
            snake = Turtle("square")
            snake.penup()
            snake.goto(i)
            snake.color("white")
            self.segments.append(snake)

    def move(self):
        """moves the snake in the coordinates of the first turtle"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_body(self, postion):
        snake = Turtle("square")
        snake.penup()
        snake.goto(postion)
        snake.color("white")
        self.segments.append(snake)

    def extend(self):
        self.add_body(self.segments[-1].position())


    # define the functions that change the direction of the snake except in opposite directions
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
