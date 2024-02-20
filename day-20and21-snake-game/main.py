from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
starting_position = [(0, 0), (-20, 0), (-40, 0)]

segments = []

# def snake_body():
#     new_snake_part = Turtle(shape="square")
#     new_snake_part.penup()
#     new_snake_part.color("white")
#     new_snake_part.goto(x=x_position, y=0)


for position in starting_position:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
