from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """displays the snake food at different positions on the screen """
        random_x_axis = random.randint(-280, 280)
        random_y_axis = random.randint(-280, 280)
        self.goto(random_x_axis, random_y_axis)



