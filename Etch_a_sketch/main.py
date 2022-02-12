# An "etch a sketch" program that uses key inputs
from turtle import Turtle, Screen

jack = Turtle()
screen = Screen()




def move_forward():
    jack.forward(10)
def move_back():
    jack.backward(10)
def move_left():
    jack.left(10)

def move_right():
    jack.right(10)

def clear_screen():
    jack.clear()
    jack.penup()
    jack.home()
    jack.pendown()
screen.listen()
screen.onkey(key = "w", fun = move_forward)
screen.onkey(key = "s", fun = move_back)
screen.onkey(key = "a", fun = move_left)
screen.onkey(key = "d", fun = move_right)
screen.onkey(key = "c", fun = clear_screen)

screen.exitonclick()