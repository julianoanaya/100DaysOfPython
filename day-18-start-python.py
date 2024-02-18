# Have to write turtle.Turtle() everytime
# import turtle
# tim = turtle.Turtle()

# imports the whole module
# from turtle import *
# forward() - confusing just seeing this - hard to read

# shorten .turtle to .t
# import turtle as t
# tim = t.Turtle()

from turtle import Screen
import turtle as t
import random


tim = t.Turtle()
tim.shape("turtle")
num_sides = 3
screen = Screen()
screen.colormode(255)
r = random.randint(1, 255)
g = random.randint(1, 255)
b = random.randint(1, 255)
tim.color(r, g, b)

# while True:
#     for _ in range(num_sides):
#         angle = 360 / num_sides
#         tim.forward(100)
#         tim.right(angle)
#         tim.color(r, g, b)
#     else:
#         num_sides += 1
#         r = random.randint(1,255)
#         g = random.randint(1,255)
#         b = random.randint(1,255)
#         if num_sides > 10:
#             break


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 11):
    draw_shape(shape_side_n)

screen.exitonclick()
