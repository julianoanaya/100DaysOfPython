from turtle import Screen, Turtle

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG")


paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.left(90)
paddle.turtlesize(0.5, 3.5)
paddle.penup()
paddle.setpos(350, 0)

screen.listen()


def move_up():
    paddle.forward(10)


def move_down():
    paddle.backward(10)


screen.listen()
screen.onkey(fun=move_up, key="Up")
screen.onkey(fun=move_down, key="Down")
screen.exitonclick()
