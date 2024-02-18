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

tim = t.Turtle()
tim.shape("turtle")
tim.color("violet")

for i in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()


screen = Screen()
screen.exitonclick()
