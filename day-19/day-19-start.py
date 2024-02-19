from turtle import Turtle, Screen

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(
    "Make your bet!", "Which turtle will win the race? Enter a color: "
)
colors = ["red", "blue", "green", "yellow", "orange", "purple"]
name = ["tim", "tom", "tat", "tem", "tam", "tum"]
y_position = [-100, -66, -33, 33, 66, 100]
# i = len(colors)
# print(i)
# tim = Turtle(shape="turtle")
# tim.color("red")
# tim.penup()
# tim.goto(x=-235, y=-100)


def make_turtle_starting_race():
    for i in range(0, 6):
        name[i] = Turtle(shape="turtle")
        name[i].color(colors[i])
        name[i].penup()
        name[i].goto(x=-235, y=y_position[i])


make_turtle_starting_race()
screen.exitonclick()
