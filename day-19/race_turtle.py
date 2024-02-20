import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(
    "Make your bet!", "Which turtle will win the race? Enter a color: "
)
colors = ["red", "blue", "green", "yellow", "orange", "purple"]
y_position = [-100, -66, -33, 33, 66, 100]
all_turtle = []


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-235, y=y_position[turtle_index])
    all_turtle.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            wining_color = turtle.pencolor()
            if wining_color == user_bet:
                print(f"You have won! The {wining_color} turtle is the winner")
            else:
                print(f"You have lost! The {wining_color} turtle is the winner")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
