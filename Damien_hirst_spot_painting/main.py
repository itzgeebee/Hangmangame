import turtle
import colorgram
import random



"""colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)"""

rgb_colors =  [ (202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

jimmy = turtle.Turtle()
turtle.colormode(255)
jimmy.ht()
jimmy.penup()
jimmy.speed("fastest")
jimmy.setheading(220)
jimmy.forward(310)
number_of_dots = 100



jimmy.setheading(0)
for i in range(1, number_of_dots + 1):
    jimmy.dot(20, random.choice(rgb_colors))
    jimmy.forward(50)
    if i % 10 == 0:
        jimmy.left(90)
        jimmy.forward(50)
        jimmy.left(90)
        jimmy.forward(500)
        jimmy.setheading(0)










screen = turtle.Screen()
screen.exitonclick()