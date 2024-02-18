# Have to write turtle.Turtle() everytime
# import turtle
# tim = turtle.Turtle()

# imports the whole module
# from turtle import *
# forward() - confusing just seeing this - hard to read

# shorten .turtle to .t
# import turtle as t
# tim = t.Turtle()

from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("violet")
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)

for i in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)
    print("Hello")


screen = Screen()
screen.exitonclick()
