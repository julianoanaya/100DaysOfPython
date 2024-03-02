from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-230, 270)
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level = {self.level}", False, "center", FONT)

    def increase_score(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", False, "center", FONT)
