from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("PONG")
screen.tracer(0)

L_paddle = Paddle((350, 0))

R_paddle = Paddle((-350, 0))

ball = Ball()

screen.listen()
screen.onkey(fun=L_paddle.move_up, key="Up")
screen.onkey(fun=L_paddle.move_down, key="Down")
screen.onkey(fun=R_paddle.move_up, key="w")
screen.onkey(fun=R_paddle.move_down, key="s")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()


screen.exitonclick()
