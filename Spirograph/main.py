# A simple program that draws a spirograph using the turtle python package
import turtle
from random import choice, random, randrange, randint

jonny = turtle.Turtle()
turtle.colormode(255)
jonny.shape("turtle")
jonny.color("blueViolet")

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rand_colors = (r, g, b)
    return rand_colors

def draw_shape(num_of_sides):
    angle = 360 / num_of_sides
    for i in range(num_of_sides):
        jonny.forward(100)
        jonny.right(angle)


directions = [0, 90, 270, 180]



def random_walk():
    move = 300
    jonny.pensize(10)
    jonny.speed(7)
    while move > 0 and move <= 300:
        jonny.forward(30)
        jonny.setheading(choice(directions))
        jonny.color(random_color())

        move -= 1
def draw_spirograph(size_of_gap):
    jonny.speed("fastest")
    for i in range(int(360/size_of_gap)):
        r = 100
        jonny.circle(r)
        jonny.setheading(jonny.heading() + size_of_gap)
        jonny.color(random_color())


draw_spirograph(5)


screen = turtle.Screen()
screen.exitonclick()
