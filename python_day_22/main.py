from turtle import Screen, Turtle

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG")


paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.turtlesize(8.5, 2.0)
paddle.penup()
paddle.setpos(350, 0)

screen.listen()
screen.exitonclick()
