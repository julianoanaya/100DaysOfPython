from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("PONG")
screen.tracer(0)

paddle_one = Paddle()
paddle_one.goto(350, 0)

paddle_two = Paddle()
paddle_two.goto(-350, 0)

screen.listen()
screen.onkey(fun=paddle_one.move_up, key="Up")
screen.onkey(fun=paddle_one.move_down, key="Down")
screen.onkey(fun=paddle_two.move_up, key="w")
screen.onkey(fun=paddle_two.move_down, key="s")


game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()
