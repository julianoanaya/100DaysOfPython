from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350, 0))

l_paddle = Paddle((-350, 0))

ball = Ball()

r_score = Scoreboard((270, 240))
l_score = Scoreboard((-270, 240))

screen.listen()
screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")
screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    "#detect collision with wall"
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    "# detect collision with paddles"
    if (
        ball.distance(r_paddle) < 50
        and ball.xcor() > 320
        or ball.distance(l_paddle) < 50
        and ball.xcor() < -320
    ):
        ball.bounce_x()

    "#detects when the paddle misses the ball"
    if ball.xcor() > 380:
        l_score.increase_score()
        ball.reset_position()
    if ball.xcor() < -380:
        r_score.increase_score()
        ball.reset_position()
screen.exitonclick()
