from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("violet")
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)

for i in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)
    print("Hello")


screen = Screen()
screen.exitonclick()
