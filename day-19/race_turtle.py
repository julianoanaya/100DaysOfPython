from turtle import Turtle, Screen

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(
    "Make your bet!", "Which turtle will win the race? Enter a color: "
)
colors = ["red", "blue", "green", "yellow", "orange", "purple"]

tim = Turtle(shape="turtle")
tim.color("red")
tim.penup()
tim.goto(x=-235, y=-100)

screen.exitonclick()
