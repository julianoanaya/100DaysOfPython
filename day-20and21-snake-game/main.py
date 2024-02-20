from turtle import Screen, Turtle

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
# tim = Turtle()
# tim.shape("square")
# tim.color("white")
starting_position = [(0, 0), (-20, 0), (-40, 0)]


# def snake_body():
#     new_snake_part = Turtle(shape="square")
#     new_snake_part.penup()
#     new_snake_part.color("white")
#     new_snake_part.goto(x=x_position, y=0)


for position in starting_position:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.goto(position)


screen.exitonclick()
